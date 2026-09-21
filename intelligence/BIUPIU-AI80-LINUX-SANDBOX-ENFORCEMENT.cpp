#include <cerrno>
#include <fcntl.h>
#include <iostream>
#include <linux/landlock.h>
#include <sys/prctl.h>
#include <sys/syscall.h>
#include <sys/wait.h>
#include <unistd.h>

#ifndef SYS_landlock_create_ruleset
#define SYS_landlock_create_ruleset 444
#endif
#ifndef SYS_landlock_restrict_self
#define SYS_landlock_restrict_self 446
#endif
#ifndef LANDLOCK_CREATE_RULESET_VERSION
#define LANDLOCK_CREATE_RULESET_VERSION (1U << 0)
#endif
#ifndef LANDLOCK_ACCESS_FS_WRITE_FILE
#define LANDLOCK_ACCESS_FS_WRITE_FILE (1ULL << 1)
#endif

static bool pass(bool v,const char* n){std::cout<<(v?"PASS ":"FAIL ")<<n<<"\n";return v;}

int main(){
  bool ok=true; errno=0;
  long abi=syscall(SYS_landlock_create_ruleset,nullptr,0,LANDLOCK_CREATE_RULESET_VERSION);
  if(abi<0 && (errno==ENOSYS || errno==EOPNOTSUPP)){
    std::cout<<"INFO landlock_unavailable_capability_only\n";
  } else if(abi<0) {
    ok&=pass(false,"landlock_version_probe");
  } else {
    ok&=pass(abi>=1,"landlock_abi_detected");
    struct landlock_ruleset_attr ruleset{};
    ruleset.handled_access_fs=LANDLOCK_ACCESS_FS_WRITE_FILE;
    int rs=(int)syscall(SYS_landlock_create_ruleset,&ruleset,sizeof(ruleset),0);
    if(rs<0) ok&=pass(false,"landlock_ruleset_create");
    else {
      int nnp=prctl(PR_SET_NO_NEW_PRIVS,1,0,0,0);
      ok&=pass(nnp==0,"no_new_privs_set");
      int rr=(int)syscall(SYS_landlock_restrict_self,rs,0);
      ok&=pass(rr==0,"landlock_ruleset_enforced");
      close(rs);

      const char* path="/tmp/biupiu-ai80-synthetic-denial";
      int pre=open(path,O_CREAT|O_WRONLY|O_TRUNC|O_CLOEXEC,0600);
      if(pre>=0) close(pre);
      errno=0;
      int denied=open(path,O_WRONLY|O_APPEND|O_CLOEXEC);
      ok&=pass(denied<0 && (errno==EACCES || errno==EPERM),"synthetic_write_denied");
      if(denied>=0) close(denied);
      unlink(path);
    }
  }

  int fd=open("/dev/null",O_RDONLY|O_CLOEXEC);
  ok&=pass(fd>=0,"readonly_fd_smoke");
  if(fd>=0) close(fd);

  pid_t pid=fork();
  if(pid==0) _exit(0);
  ok&=pass(pid>0,"child_creation_smoke");
  if(pid>0){int st=0; ok&=pass(waitpid(pid,&st,0)==pid && WIFEXITED(st),"child_wait_smoke");}

  std::cout<<(ok?"AI80_RESULT=PASS\n":"AI80_RESULT=FAIL\n");
  return ok?0:1;
}

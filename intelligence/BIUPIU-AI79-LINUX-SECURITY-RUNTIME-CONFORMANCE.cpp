#include <cerrno>
#include <fcntl.h>
#include <iostream>
#include <sys/prctl.h>
#include <sys/syscall.h>
#include <unistd.h>

#ifndef SYS_landlock_create_ruleset
#define SYS_landlock_create_ruleset 444
#endif
#ifndef LANDLOCK_CREATE_RULESET_VERSION
#define LANDLOCK_CREATE_RULESET_VERSION (1U << 0)
#endif

static bool p(bool v,const char* n){std::cout<<(v?"PASS ":"INFO ")<<n<<"\n";return v;}

int main(){
  bool ok=true;
  errno=0;
  long abi=syscall(SYS_landlock_create_ruleset,nullptr,0,LANDLOCK_CREATE_RULESET_VERSION);
  if(abi>=0) ok &= p(true,"landlock_abi_detected");
  else if(errno==ENOSYS || errno==EOPNOTSUPP) p(true,"landlock_absent_capability_detected");
  else ok &= p(false,"landlock_probe_error");

  errno=0;
  int nnp=prctl(PR_GET_NO_NEW_PRIVS,0,0,0,0);
  ok &= p(nnp==0 || nnp==1,"no_new_privs_probe");

  int fd=open("/dev/null",O_RDONLY|O_CLOEXEC);
  ok &= p(fd>=0,"readonly_fd_smoke");
  if(fd>=0) close(fd);

  std::cout<<(ok?"AI79_RESULT=PASS\n":"AI79_RESULT=FAIL\n");
  return ok?0:1;
}
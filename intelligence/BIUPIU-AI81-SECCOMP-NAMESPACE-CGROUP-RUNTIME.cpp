#include <cerrno>
#include <fcntl.h>
#include <iostream>
#include <linux/filter.h>
#include <linux/seccomp.h>
#include <sched.h>
#include <sys/prctl.h>
#include <sys/syscall.h>
#include <sys/types.h>
#include <unistd.h>

#ifndef SECCOMP_RET_KILL_PROCESS
#define SECCOMP_RET_KILL_PROCESS SECCOMP_RET_KILL
#endif

static bool pass(bool v,const char* n){std::cout<<(v?"PASS ":"FAIL ")<<n<<"\n";return v;}

int main(){
  bool ok=true;

  // Seccomp: install a synthetic filter that denies only getpid with EPERM.
  struct sock_filter filter[] = {
    BPF_STMT(BPF_LD|BPF_W|BPF_ABS, offsetof(struct seccomp_data, arch)),
#if defined(__x86_64__)
    BPF_JUMP(BPF_JMP|BPF_JEQ|BPF_K, AUDIT_ARCH_X86_64, 0, 1),
#elif defined(__aarch64__)
    BPF_JUMP(BPF_JMP|BPF_JEQ|BPF_K, AUDIT_ARCH_AARCH64, 0, 1),
#else
    BPF_STMT(BPF_JMP|BPF_JA, 0),
#endif
    BPF_STMT(BPF_RET|BPF_K, SECCOMP_RET_ALLOW),
    BPF_STMT(BPF_LD|BPF_W|BPF_ABS, offsetof(struct seccomp_data, nr)),
    BPF_JUMP(BPF_JMP|BPF_JEQ|BPF_K, SYS_getpid, 0, 1),
    BPF_STMT(BPF_RET|BPF_K, SECCOMP_RET_ERRNO | EPERM),
    BPF_STMT(BPF_RET|BPF_K, SECCOMP_RET_ALLOW)
  };
  struct sock_fprog prog{static_cast<unsigned short>(sizeof(filter)/sizeof(filter[0])),filter};

  ok&=pass(prctl(PR_SET_NO_NEW_PRIVS,1,0,0,0)==0,"no_new_privs_set");
  ok&=pass(prctl(PR_SET_SECCOMP,SECCOMP_MODE_FILTER,&prog)==0,"seccomp_filter_installed");

  errno=0;
  long pid=syscall(SYS_getpid);
  ok&=pass(pid==-1 && errno==EPERM,"synthetic_syscall_denied");

  // Namespace visibility: no mutation; only inspect namespace handles.
  int nsfd=open("/proc/self/ns/user",O_RDONLY|O_CLOEXEC);
  ok&=pass(nsfd>=0,"user_namespace_visibility");
  if(nsfd>=0)close(nsfd);

  int pidns=open("/proc/self/ns/pid",O_RDONLY|O_CLOEXEC);
  ok&=pass(pidns>=0,"pid_namespace_visibility");
  if(pidns>=0)close(pidns);

  // Cgroup visibility: read-only v2 controller inventory when available.
  int cg=open("/sys/fs/cgroup/cgroup.controllers",O_RDONLY|O_CLOEXEC);
  if(cg>=0){ char b[256]; ssize_t n=read(cg,b,sizeof(b)-1); ok&=pass(n>=0,"cgroup_v2_visibility"); close(cg); }
  else if(errno==ENOENT || errno==EACCES || errno==EPERM) std::cout<<"INFO cgroup_v2_unavailable_or_restricted\n";
  else ok&=pass(false,"cgroup_visibility_probe");

  std::cout<<(ok?"AI81_RESULT=PASS\n":"AI81_RESULT=FAIL\n");
  return ok?0:1;
}

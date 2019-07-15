#!/usr/bin/python
from bcc import BPF
from bcc.utils import printb

bpf_source = """
#include <uapi/linux/ptrace.h>

BPF_PERF_OUTPUT(events);

struct data_t {
    char comm[16];
};

int do_sys_execve(struct pt_regs *ctx,
    const char __user *filename,
    const char __user *const __user *__argv,
    const char __user *const __user *__envp)
{
  struct data_t data = {};
  bpf_get_current_comm(&data.comm, sizeof(data.comm));

  events.perf_submit(ctx, &data, sizeof(data));
  return 0;
}
"""

def dump_data(cpu, data, size):
    event = bpf["events"].event(data)
    printb(b"%-16s" % event.comm)

bpf = BPF(text = bpf_source)
execve_function = bpf.get_syscall_fnname("execve")
bpf.attach_kprobe(event = execve_function, fn_name = "do_sys_execve")

bpf["events"].open_perf_buffer(dump_data)
while 1:
    bpf.perf_buffer_poll()

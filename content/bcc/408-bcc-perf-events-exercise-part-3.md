---
title:  "bcc-perf-events-exercise-3"
weight: 407
---

# BCC perf events exercise (part 3)
.exercise[
```
from bcc import BPF
from bcc.utils import printb

def dump_data(cpu, data, size):
    event = bpf["events"].event(data)
    printb(b"%-16s" % event.comm)

bpf = BPF(text = bpf_source)
execve_function = bpf.get_syscall_fnname("execve")
bpf.attach_kprobe(event = execve_function, fn_name = "on_execve")

bpf["events"].open_perf_buffer(dump_data)
while 1:
    bpf.perf_buffer_poll()
```
]

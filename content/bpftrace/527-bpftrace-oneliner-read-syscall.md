
---
title:  "bpftrace-oneliners-read-syscall"
weight: 527
class: extra-details
---

# bpftrace hands on: tracing read bytes using a tracepoint

- We want to do the same thing we did with the `kretprobe` in the previous exercise

.exercise[
- Execute this one liner using bpftrace
```bash
bpftrace -e 'tracepoint:syscalls:sys_exit_read  { @bytes = lhist(args->ret, 0, 2000, 200); }'
```
- Let it run for a while then use `Ctrl-C` to dump the results
]

**What's the difference?**
While being very powerful (it can trace any kernel function), `kretprobe` approach can't be considered "stable", because internal 
kernel functions can change between kernels. On the other hand using a tracepoint is a much more stable approach because tracepoints
are considered as a user facing feature and not an internal one by kernel developers.
Whenever possible use tracepoints instead of kprobe/kretprobe.



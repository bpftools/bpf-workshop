---
title:  "exercise example"
weight: 999
class: extra-details
---

## Exercise example

.exercise[
Write this code in a file called test.bt
```
tracepoint:syscalls:sys_enter_read
{
  @start[tid] = nsecs;
}

tracepoint:syscalls:sys_exit_read / @start[tid] /
{
  @times = hist(nsecs - @start[tid]);
  delete(@start[tid]);
}
```
Execute it with 
```bash
bpftrace read.bt
```
]

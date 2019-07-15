---
title:  "bcc-perf-events-exercise-1"
weight: 406
---

# BCC perf events exercise (part 1)

.exercise[
```
bpf_source = """
int on_execve(struct pt_regs *ctx,
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
```
]

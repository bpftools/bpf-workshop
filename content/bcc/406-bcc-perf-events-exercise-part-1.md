---
title:  "bcc-perf-events-exercise-1"
weight: 406
---

# BCC perf events exercise (part 1)

.exercise[
```
bpf_source = """
#include <uapi/linux/ptrace.h>

BPF_PERF_OUTPUT(events);

struct data_t {
    char comm[16];
};
"""
```
]

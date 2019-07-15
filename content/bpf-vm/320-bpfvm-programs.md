---
title:  "bpfvm-bpf-programs"
weight: 320
---

# BPF programs

- Code that's triggered based on events in the kernel
- Context arguments that depend on the event triggered
- Must always terminate
- Cannot include outbounded control loops
- Limited in the number of instructions to execute (changing soon)
- Can trigger other BPF programs

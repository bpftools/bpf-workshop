---
title:  "bpftrace-intro"
weight: 501
---

# bpftrace: BPF observability front-end

On GitHub https://github.com/iovisor/bpftrace

*What it is*:

- Higher level language to write eBPF programs;
- Built from the ground-up for BPF and Linux;
- Used in production at Netflix, Facebook, etc;
- Custom one-liners;
- Comes with tools;
- It is just for tracing;

*What it is NOT*:

- A framework to build your loaders;
- You can't do classic bpf with it (like seccomp programs or socket probe types);
- It does not support traffic control and XDP;



---
title:  "bpfvm-explaination"
weight: 301
---

# The BPF in-kernel Virtual Machine

- Implements a general purpose lowe level RISC instructions
- Runs the instructions in response to events triggered by the kernel
- Implements a verifier, so that your programs can't break the kernel
- Has different interfaces for different types of programs
- Widely supported in the kernel
- Has an upstream LLVM backend, you can compile eBPF code with clang

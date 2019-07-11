---
title:  "security-lsm"
weight: 1102
class: extra-details
---

# LSM Hooks

- The Linux security modules (LSM) framework, has a set of hooks to control the execution of (e)BPF programs,
- Allows to create a fine-grained set of privileges around them when using a module that implements BPF hooks support
- Actually implemented by Landlock and SELinux
- The only in kernel tree implementation is SELinux
- It's based on the concept of hook calls instead of syscalls

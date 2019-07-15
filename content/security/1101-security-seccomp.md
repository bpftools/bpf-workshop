---
title:  "security-seccomp"
weight: 1101
class: extra-details
---

# Seccomp

- Stands for Secure Computing; 
- Implements a filtering backend based on cBPF
- You can write a BPF program hat filters the execution of any syscall by allowing/disallowing the ones you want based on your logic;

Here's the seccomp data structure for filters as from `linux/seccomp.h`

```c
struct seccomp_data {
	int nr;
	__u32 arch;
	__u64 instruction_pointer;
	__u64 args[6];
}; 
```

Allows to filter based on: the system call, its arguments or a combination of them.


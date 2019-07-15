---
title:  "bcc-hello-world-destilled"
weight: 404
---

# BCC hello world destilled

```
source = """
int kprobe__sys_clone(void *ctx) {
  bpf_trace_printk("Hello, World!\n");
  return 0;
}
"""

BPF(text = source).trace_print()
```

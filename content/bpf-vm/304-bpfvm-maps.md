---
title:  "bpfvm-bpf-maps"
weight: 304
---

# Maps

- BPF Maps data stores that live in the kernel;
- Can be accessed by any BPF program that knows about them;
- Programs that run in user-space can also access these maps by using file descriptors;
- You can store any kind of data in a map, as long as you specify the data size correctly before hand;
- The kernel treats keys and values as binary blobs and it doesn’t care about what you keep in a map;
- This is what we use to let userspace programs to extract or feed information into BPF programs running in the kernel!


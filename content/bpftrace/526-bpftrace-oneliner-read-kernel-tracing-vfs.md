
---
title:  "bpftrace-oneliners-read-kernel-tracing-vfs"
weight: 526
class: extra-details
---

# bpftrace hands on: tracing read bytes using a kretprobe

- We will use the capability of bpftrace to instrument the `vfs_read` function in the kernel using a `kretprobe`;
- We will create an array called `bytes` that will dump a linear histogram  where the arguments are: value, min, max, step. The first argument (retval) of vfs_read() is the return value: the number of bytes read;

.exercise[
- Execute this one liner using bpftrace, then let it run for a while then use `Ctrl-C` to dump the results
```bash
bpftrace -e 'kretprobe:vfs_read { @bytes = lhist(retval, 0, 2000, 200); }'
```
]

.footnote[.smaller[
In Linux, all files are accessed through the Virtual Filesystem Switch, or VFS, a layer of code which implements generic filesystem actions and vectors requests to the correct specific code to handle the request.
]]



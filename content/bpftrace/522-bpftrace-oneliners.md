
---
title:  "bpftrace-oneliners"
weight: 522
class: extra-details
---

# bpftrace: One-liners


**Count VFS calls**
```bash
bpftrace -e 'kprobe:vfs_* { @[func]++ }'
```

**Trace user-level function**
```bash
bpftrace -e 'uretprobe:bash:readline { printf(“%s\n”, str(retval)) }’
```

**Show vfs_read latency as a histogram**
```bash
bpftrace -e 'k:vfs_read { @[tid] = nsecs }
    kr:vfs_read /@[tid]/ { @ns = hist(nsecs - @[tid]); delete(@tid) }’
```

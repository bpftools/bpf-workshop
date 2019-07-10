---
title:  "bpftrace-builtin-variables"
weight: 520
---

# bpftrace: Builtin Variables

| variable             | description                                        |
|----------------------|----------------------------------------------------|
| tid                  | Thread ID (kernel pid)                             |
| cgroup               | Cgroup ID of the current process                   |
| uid                  | User ID                                            |
| gid                  | Group ID                                           |
| nsecs                | Nanosecond timestamp                               |
| elapsed              | Nanosecond timestamp since bpftrace initialization |
| cpu                  | Processor ID                                       |
| comm                 | Process name                                       |

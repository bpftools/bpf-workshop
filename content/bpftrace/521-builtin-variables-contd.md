---
title:  "bpftrace-builtin-variables-contd"
weight: 521
---

# bpftrace: Builtin Variables (cont'd)

| variable             | description                                        |
|----------------------|----------------------------------------------------|
| pid                  | Process ID (kernel tgid)                           |
| stack                | Kernel stack trace                                 |
| ustack               | User stack trace                                   |
| arg0, arg1, ... etc. | Arguments to the function being traced             |
| retval               | Return value from function being traced            |
| func                 | Name of the function currently being traced        |
| probe                | Full name of the probe                             |
| curtask              | Current task_struct as a u64                       |
| rand                 | Random number of type u32                          |
| $1, $2, ... etc.     | Positional parameters to the bpftrace program      |

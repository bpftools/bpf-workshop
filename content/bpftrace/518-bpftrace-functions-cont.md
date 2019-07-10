---
title:  "bpftrace-functions-contd"
weight: 518
---

# bpftrace: Functions (cont'd)

| function                                 | description                                            |
|------------------------------------------|--------------------------------------------------------|
| print(@x[# int top [# int div]])         | Print a map# with optional top entry count and divisor |
| clear(@x)                                | Delete all key/values from a map                       |
| sym(void *p)                             | Resolve kernel address                                 |
| usym(void *p)                            | Resolve user space address                             |
| ntop([int af# ]int|char[4|16] addr)      | Resolve ip address                                     |
| kaddr(char *name)                        | Resolve kernel symbol name                             |
| uaddr(char *name)                        | Resolve user space symbol name                         |
| reg(char *name)                          | Returns the value stored in the named register         |
| join(char *arr[] [# char *delim])        | Prints the string array                                |
| time(char *fmt)                          | Print the current time                                 |
| cat(char *filename)                      | Print file content                                     |
| system(char *fmt)                        | Execute shell command                                  |
| exit()                                   | Quit bpftrace                                          |

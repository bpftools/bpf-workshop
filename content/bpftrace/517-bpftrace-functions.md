---
title:  "bpftrace-functions"
weight: 517
---

# bpftrace: Functions

| function                                 | description                                            |
|------------------------------------------|--------------------------------------------------------|
| hist(int n)                              | Produce a log2 histogram of values of n                |
| lhist(int n# int min# int max# int step) | Produce a linear histogram of values of n              |
| count()                                  | Count the number of times this function is called      |
| sum(int n)                               | Sum this value                                         |
| min(int n)                               | Record the minimum value seen                          |
| max(int n)                               | Record the maximum value seen                          |
| avg(int n)                               | Average this value                                     |
| stats(int n)                             | Return the count# average# and total for this value    |
| delete(@x)                               | Delete the map element passed in as an argument        |
| str(char *s [# int length])              | Returns the string pointed to by s                     |
| printf(char *fmt# ...)                   | Print formatted to stdout                              |

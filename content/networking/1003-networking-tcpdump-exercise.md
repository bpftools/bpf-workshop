---
title:  "networking-tcpdump-exercise"
weight: 1003

---

# hands on: Tcpdump packet filtering

.exercise[
In a new terminal, execute `tcpdump` with a filter and use the `-d` option to dump the generated BPF assembly.

```bash
tcpdump  -d  'ip and tcp port 8080'
```
What do you see? Anything noteworthy?
]


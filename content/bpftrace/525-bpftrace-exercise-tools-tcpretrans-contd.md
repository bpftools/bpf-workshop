---
title:  "bpftrace-exercise-tools-tcpretrans-contd"
weight: 525
class: extra-details
---

## bpftrace hands on: Trace or count TCP retransmits (cont'd)

.exercise[
- In the `bpftrace/tools` folder;
- With root permissions;
- Execute the `tcpretrans.bt` tool;

```bash
  bpftrace tcpretrans.bt
```
- Once it's started, the best way to trigger some retransmits is to try to connect to a closed port;
- Try it on a new terminal while leaving `tcpretrans.bt` active!

```bash
  telnet bpf.sh 9090
```
]

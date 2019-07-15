---
title:  "networking-traffic-control"
weight: 1006

---

# Traffic Control (tc) and eBPF

- tc is the kernel packet scheduling subsystem;
- It's made  of mechanisms and queuing systems that decide how packet flows and are accepted into the system;
- It has a classifier that can use a bpf program to make the decisions, called `cls_bpf`;

Among tc use cases there are:

- Prioritize certain kinds of packets
- Drop specific kind of packet
- Bandwidth distribution



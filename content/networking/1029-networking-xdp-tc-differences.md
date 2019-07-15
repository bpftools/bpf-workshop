---
title:  "networking-xdp-tc-differences"
weight: 1029
---

# Differences between TC and XDP

- XDP programs are executed earlier in the ingress data path, before entering in the main kernel network stack;
- Program does not have access to a Socket buffer struct sk_buff like with tc;
- XDP programs instead take a different structure called xdp_buff that is an eager representation of the packet without metadata;

**All this comes with advantages and disadvantages**:

Being executed even before the kernel code, XDP programs can drop packets in a very efficient way. Compared to tc programs, XDP programs can only be attached to traffic in ingress to the system. 

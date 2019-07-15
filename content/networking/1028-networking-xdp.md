---
title:  "networking-xdp"
weight: 1029
---

# Xpress Data Path

- Programs are of type `BPF_PROG_TYPE_XDP`
- There are three operation modes:
  - *Native:* the network card driver supports XDP, code runs on the driver receive path;
  - *Offloaded:* the network card hardware supports XDP, the nic CPU will execute the logic;
  - *Generic:* It's provided as a test mode for developers it's for testing xdp programs without having the proper hardware;
- Once packets are processed, XDP will return one of its possible codes:
  - *XDP_DROP*: drop the packet;
  - *XDP_TX*: forward the packet;
  - *XDP_REDIRECT*: similar to TX but forward to another nic or map of type CPU map; 
  - *XDP_PASS*: allow the packet

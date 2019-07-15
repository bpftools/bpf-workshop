---
title:  "networking-xdp-interactions"
weight: 1030
---

# XDP packets processor

.footnote[.smaller[
- It executes BPF programs for XDP packets
- Coordinates the interaction between them and the network stack
- It ensures that packets are read and writeable and allows to attach post processing verdicts in the form of packet processor actions
- The illustrated return codes before, are its return actions!

  ]]
.pic[
![xdp packets processor](/img/xdp-interaction-diagram.png)
]


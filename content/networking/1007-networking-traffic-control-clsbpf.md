---
title:  "networking-traffic-control"
weight: 1007

---

# Traffic Control cls_bpf hook points

- cls_bpf can hook in ingress and egress
- that means that you can manipulate both packets your machine receives and packets it sends!
- programs receive an `sk_buff`

Here's a diagram showing the interactions:

.pic[![cls_bpf interactions](/img/tc-flow-bpf-cls.png)]

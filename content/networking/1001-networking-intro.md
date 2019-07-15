---
title:  "networking-intro"
weight: 1001

---

# eBPF and Linux Networking

**Main use cases**

- Retrospective analysis of network traffic captured on a live system, using the pcap format for example;
- Live packet filtering, e.g: allow only UDP traffic and discard anything else;
- Live observation of a filtered set of packets flowing into a live system;


**At different levels**

- cBPF packet filtering
- Raw packet filtering (`BPF_PROG_TYPE_SOCKET_FILTER`)
- Traffic control
- XDP


---
title:  "bpftrace-exercise-tools-tcpretrans"
weight: 524
class: extra-details
---

## bpftrace hands on: Trace or count TCP retransmits

- In the bpftrace tools folder, there's a tool called `tcpretrans.bt`;
- TCP wants to make sure that your packet is received with the *guarantee* that all the received bytes will be identical and in the same order as those sent,
this technique is called **positive acknowledgement with re-transmission**;
- What happens when there are many retransmits is that your system can have a significant overhead, then you want to know when a retransmit occurs, `tcpretrans.bt` does just that
- Retransmits are usually a sign of poor network health, and this tool is
useful for their investigation. Unlike using tcpdump, this tool has very
low overhead, as it only traces the retransmit function. It also prints
additional kernel details: the state of the TCP session at the time of the
retransmit.


---
title:  "networking-tcpdump"
weight: 1002

---

# cBPF and packet filtering

- Packet filtering is done using an accumulator on which filters are applied, the classic BPF way;
- One of the most popular use cases for it is `tcpdump`;
- It doesn't support the use of maps;

**Tcpdump**

- Probably the most known use cases for live packets observation;
- It is implemented as a frontend for `libpcap`;
- Allows to define high level filtering expression that are then converted to a BPF filtering expression;
- Tcpdump can dump the used BPF for user inspection;
- Can read from an existing pcap file and filter on it


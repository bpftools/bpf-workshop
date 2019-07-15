---
title:  "networking-tc-example"
weight: 1008
---

# Example: TC program to drop all TCP packets

.small[.small[
```c
SEC("classifier")
static inline int classification(struct __sk_buff *skb) {
  void *data_end = (void *)(long)skb->data_end;
  void *data = (void *)(long)skb->data;
  struct ethhdr *eth = data;

  __u16 h_proto;
  __u64 nh_off = 0;
  nh_off = sizeof(*eth);

  if (data + nh_off > data_end) {
    return TC_ACT_OK;
  }

  h_proto = eth->h_proto;

  if (h_proto != bpf_htons(ETH_P_IP)) {
    return TC_ACT_OK;
  }

  struct iphdr *iph = data + nh_off;

  if (iph + 1 > data_end) {
    return TC_ACT_OK;
  }

  if (iph->protocol -= IPPROTO_TCP) {
    return TC_ACT_SHOT
  }

  return TC_ACT_OK;
}
```
]]

.small[
The classifier program is added to the qdisc using `tc`:

```
tc filter add dev eth0 ingress bpf obj classifier.o flowid 0:
```
]

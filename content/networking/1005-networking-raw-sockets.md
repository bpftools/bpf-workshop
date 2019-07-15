---
title:  "networking-raw-packets"
weight: 1005

---

# Raw packets filtering

- Attach a BPF program to a socket
- All the packets received by it will be to the program as an `sk_buff` struct
- The program can make the decision on whether to discard or allow them based on its logic


Here's an example, the program type is given by the `SEC("socket")` definition that gets translated to `BPF_PROG_TYPE_SOCKET_FILTER`.

.small[
```c
SEC("socket")
int socket_prog(struct __sk_buff *skb) {
  int proto = load_byte(skb, ETH_HLEN + offsetof(struct iphdr, protocol));
  int one = 1;
  int *el = bpf_map_lookup_elem(&countmap, &proto);
  if (el) {
    (*el)++;
  } else {
    el = &one;
  }
  bpf_map_update_elem(&countmap, &proto, el, BPF_ANY);
  return 0;
}
```
]

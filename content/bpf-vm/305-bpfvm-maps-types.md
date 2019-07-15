---
title:  "bpfvm-bpf-maps-types"
weight: 305
---

**Many different types of maps**

- Hash table: BPF_MAP_TYPE_HASH
- Array: BPF_MAP_TYPE_ARRAY
- Program array maps: BPF_MAP_TYPE_PROG_ARRAY, this one is magic, allows you to store references to bpf programs so that you can do jumps between bpf programs;
- Perf events array maps: BPF_MAP_TYPE_PERF_EVENT_ARRAY
- Per-CPU hash maps: BPF_MAP_TYPE_PERCPU_HASH
- Per-CPU array maps: BPF_MAP_TYPE_PERCPU_ARRAY
- Stack trace maps: BPF_MAP_TYPE_STACK_TRACE
- Cgroup array maps: BPF_MAP_TYPE_CGROUP_ARRAY
- Hash and per cpu has with LRU cache: BPF_MAP_TYPE_LRU_PERCPU_HASH, BPF_MAP_TYPE_LRU_HASH
- Longest Prefix Match(LPM) Trie: BPF_MAP_TYPE_LPM_TRIE
- Array of maps, and hash of maps, maps: `BPF_MAP_TYPE_ARRAY_OF_MAPS` and `BPF_MAP_TYPE_HASH_OF_MAPS`
- And many more! Find all of them `man 2 bpf`

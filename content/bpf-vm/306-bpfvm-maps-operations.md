---
title:  "bpfvm-bpf-maps-operations"
weight: 306
---

**Maps operations**

- Lookup a single element value, `bpf_map_lookup_elem`
- Remove an element, `bpf_map_delete_element`
- Iterating over elements
- Updating an element, `bpf_map_update_elem`
- Get the next key in the map, `bpf_map_get_next_key`
- Search, get the value and delete in a single atomic operation, `bpf_map_lookup_and_delete_element`
- Concurrent access is regulated using a mechanism called `bpf_spin_lock` that is essentially a semaphore;

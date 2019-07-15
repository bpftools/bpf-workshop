---
title:  "bcc-profile-exercise"
weight: 412
---

# BCC Profile exercise (Part 2)

.exercise[
- Download the Flamegrapsh scripts:

```
git clone https://github.com/brendangregg/FlameGraph
```

- Generate a flamegraph for your profiled data:

```
sudo tools/profile -p PID -f > /tmp/profile.out

flamegraph.pl /tmp/profile.out > /tmp/profile-graph.svg \
  && firefox /tmp/profile-graph.svg
```
]

---
title:  "bpftrace-install"
weight: 502
---

# bpftrace: Installation

We will need to do some exercises with bpftrace.
If you are not using the Vagrant environment, you might want to install it now!

Ubuntu snap package

```
sudo snap install --devmode bpftrace
sudo snap connect bpftrace:system-trace
```

Fedora (28 or later)

```
sudo dnf install bpftrace
```

You can find further instructions [here](https://github.com/iovisor/bpftrace/blob/master/INSTALL.md)



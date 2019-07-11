---
title:  "kubernetes-just-a-container"
weight: 710

---

# Approach #1: Just use a container

- A sidecar container sharing the process namespace;
- You just provide an image with eBPF loader as entrypoint;
- The loader will just load the program and execute it;
- Not extremely generic but does the job!
- A very flexible approach!

.small[.small[
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: happy-borg
spec:
  shareProcessNamespace: true
  containers:
  - name: execsnoop
    image: calavera/execsnoop
    securityContext:
    - privileged: true
    volumeMounts:
    - name: sys # mount the debug filesystem
      mountPath: /sys
      readOnly: true
    - name: headers # mount the kernel headers required by bcc
      mountPath: /usr/src
      readOnly: true
    - name: modules # mount the kernel modules required by bcc
      mountPath: /lib/modules
      readOnly: true
  - name: container doing random work
  ...
```
]]

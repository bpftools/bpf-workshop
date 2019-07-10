
---
title:  "bpftrace-oneliners-uretprobe-contd"
weight: 529
class: extra-details
---

# bpftrace hands on: reading userspace returns
.exercise[
- Create a file named `main.go` with the code from [previous slide](#bpftrace-oneliners-uretprobe);
- Then, compile it with: 
```bash
  go build -o randomnumbers main.go
```
- This will create a binary named `randomnumbers` in the current folder;
- Once that is done, we just start the program `./randomnumbers`;
- Now, in a new terminal, we instrument the program using bpftrace and a `uretprobe`:

```bash
bpftrace -e \
  'uretprobe:./randomnumbers:"main.giveMeNumber"
  { printf("%d\n", retval) }'
```
]

.footnote[.smaller[Bonus point! Try to do an `objdump -t randomnumbers | grep -i giveMe`, what do you notice?]]


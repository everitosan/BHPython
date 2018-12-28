from arguments import parse_args
from scapy.all import conf
import sys
from ARPSpoofing import ARPSpoofer


def main():
    args = parse_args()

    conf.verb = 0

    spoofer = ARPSpoofer()
    spoofer.set_target(args.target)
    spoofer.set_gateway(args.gateway)

    spoofer.spoof()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("bye bye!")

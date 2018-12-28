import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Arguments to ARP Poison")
    parser.add_argument(
        "-t",
        "--target",
        type=str,
        required=True
    )
    parser.add_argument(
        "-gt",
        "--gateway",
        type=str,
        required=True
    )
    parser.add_argument(
        "-if",
        "--interface",
        type=str,
        required=True
    )
    return parser.parse_args()

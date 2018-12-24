from client import run_client
from Server import run_server
import sys


def main():
    mode = "client"
    if (sys.argv[1] == "-s"):
        mode = "server"

    if mode == "client":
        run_client(sys.argv[2], sys.argv[3])
    else:
        run_server()


if __name__ == "__main__":
    main()

import sys
from server import serverloop


def main():
    print("Python proxy")
    n_params = len(sys.argv[1:])
    print
    if n_params != 5:
        print("Usage: ./05Proxy [localhost][localport][remotehost][remoteport][receivefirst]")
        sys.exit(0)

    local_host = sys.argv[1]
    local_port = int(sys.argv[2])
    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])
    receive_first = True if sys.argv[5] == "True" else False

    serverloop(local_host, local_port, remote_host, remote_port, receive_first)


if __name__ == "__main__":
    main()

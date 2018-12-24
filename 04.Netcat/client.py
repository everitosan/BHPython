import socket
import sys


def getClient():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(("0.0.0.0", 8888))
        return client
    except:
        print("[*] Error ...exiting")
        client.close()
        sys.exit(0)


def start_shell(buffer):
    client = getClient()

    if len(buffer):
        client.send(buffer)

    while True:
        res = ""
        recv_len = 1

        while recv_len:
            data = client.recv(10)
            recv_len = len(data)
            res += data

            if recv_len < 10:
                break

        print(res)

        buffer = raw_input("")
        buffer += "\n"

        client.send(buffer)

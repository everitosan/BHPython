import sys
import socket
import getopt
import threading
import subprocess

from usage import usage
from client import start_shell
from server import server_loop

# variables globales
# acciones
listen = False
command = False
upload = False
#
excecute = ""
target = ""
upload_destination = ""
port = 0


def main():
    global listen
    global port
    global execute
    global target
    global command
    global upload_destination

    script_params = sys.argv[1:]

    if not len(script_params):
        usage()

    try:
        opts, args = getopt.getopt(
            script_params,
            "hle:t:p:cu",
            ["help", "listen", "excecute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print("*"*30)
        print(str(err))
        print("*"*30)
        usage()

    for o, a in opts:
        if o in ["-h", "--help"]:
            usage()
        elif o in ["-l", "--listen"]:
            listen = True
        elif o in ["-e", "--exceute"]:
            exceute = a
        elif o in ["-t", "--target"]:
            target = a
        elif o in ["-p", "--port"]:
            port = int(a)
        elif o in ["-u", "--upload"]:
            upload_destination = a
        else:
            assert False, "unhandled option"

    if not listen and len(target) and port > 0:
        buffer = sys.stdin.read()
        start_shell(buffer)
    if listen:
        server_loop(target, port)


if __name__ == "__main__":
    main()

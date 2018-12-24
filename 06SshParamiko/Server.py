import socket
import paramiko
import sys
import threading


class Server(paramiko.ServerInterface):

    def __init__(self):
        self.event = threading.Event()

    def check_channel(self, kind, chanid):
        print(paramiko.OPEN_SUCCEEDED)
        print("chanid: " + chanid)
        print("kind: " + kind)
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, u, p):
        if u == "StJimmy" and p == "isback":
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED


def start(server):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server['addr'], server['port']))
        sock.listen(100)
        print("[+] Listening for connection ...")
        client, addr = sock.accept()
        print("[+] Got a connection from {} : {}".format(addr[0], addr[1]))

    except Exception, e:
        print("[-] Listen failed: {}".format(str(e)))
        sys.exit(1)

    try:
        bhSession = paramiko.Transport(client)
        host_key = paramiko.RSAKey(filename="test_rsa.key")
        bhSession.add_server_key(host_key)
        server = Server()

        try:
            bhSession.start_server(server=server)
        except paramiko.SSHException as x:
            print("[-] SSh negotiation failed!")

        chan = bhSession.accept(20)
        if chan is None:
            print("[-] No Channel")
            bhSession.close()
        else:
            print("[+] Authenticated ")
            print(chan.recv(1024))
            chan.send("Welcome to Paramiko Ssh")

        while True:
            try:
                command = raw_input("Enter command: ").strip("\n")
                chan.send(command)
                if command != "exit":
                    print(chan.recv(1024))
                else:
                    print("[+] exiting ...")
                    bhSession.close()
                    break
            except Exception, e:
                print("[-] Caugt exception: {}".format(str(e)))
                bhSession.close()
                sys.exit(1)
    except Exception, e:
        print(str(e))


def run_server():
    params = sys.argv[1:]
    if len(params) < 3:
        print("Usage: python 06SshParamiko.py 127.0.0.1 22")
        sys.exit(0)
    else:
        SERVER = {}
        SERVER["addr"] = sys.argv[2]
        SERVER["port"] = int(sys.argv[3])

        start(SERVER)

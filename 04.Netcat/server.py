import socket
import threading
import subprocess


def client_handler(socket):
    while True:
        socket.send("<BHP:#> ")

        cmd_buffer = ""
        while "\n" not in cmd_buffer:
            cmd_buffer += socket.recv(1024)

        cmd = cmd_buffer.rstrip()
        try:
            res = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as err:
            res = str(err)

        print("Command: {}".format(cmd))
        print(res)
        socket.send(res)
        # socket.close()


def server_loop(target="0.0.0.0", port=8888):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)

    print("[*]Listening on {}:{}".format(target, port))

    while True:
        client_socket, addr = server.accept()
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()

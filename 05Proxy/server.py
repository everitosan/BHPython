import socket
import threading
from proxy import receive_from, response_handler, request_handler
from hexdump import hexdump


def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))
    print("Connecting to server at {}:{}".format(remote_host, remote_port))

    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)
        remote_buffer = response_handler(remote_buffer)

        if remote_buffer:
            print("[<==] Sending {} bytes to localhost ".format(len(remote_buffer)))
            client_socket.send(remote_buffer)

    while True:
        local_buffer = receive_from(client_socket)
        local_buffer_len = len(local_buffer)

        print("Reading from client")
        if local_buffer_len:
            print("[==>] Received {} bytes from localhost".format(local_buffer_len))
            hexdump(local_buffer)
            local_buffer = request_handler(local_buffer)
            remote_socket.send(local_buffer)
            print("[==>] Sent to remote")

        print("Reading from remote")
        remote_buffer = receive_from(remote_socket)
        remote_buffer_len = len(remote_buffer)
        if remote_buffer_len:
            print("[<==] Received {} bytes from remote".format(remote_buffer_len))
            hexdump(remote_buffer)

            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)
            print("[<==] Sent to localhost")

        if not local_buffer_len or not remote_buffer_len:
            client_socket.close()
            remote_socket.close()
            print("[*] No more data ... closing now")
            break


def serverloop(local_host, local_port, remote_host, remote_port, receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((local_host, local_port))
    print("Starting server at {}:{}".format(local_host, local_port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        print("[==>] Recived incoming from {} {}".format(addr[0], addr[1]))

        proxy_thread = threading.Thread(
            target=proxy_handler,
            args=(client_socket, remote_host, remote_port, receive_first))
        proxy_thread.start()

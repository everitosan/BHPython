# coding=utf-8
import socket
import threading

bindIP = "0.0.0.0"
bindPort = 9999


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print "[*] Received %s " % request
    # send back a packet
    client_socket.send("ACK!")
    client_socket.close()


# creamos un socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# le asignamos la ip y el puerto a escuchar
server.bind((bindIP, bindPort))
# especificamos n clientes máximos
server.listen(5)
print "[*] Listening on http://%s:%d" % (bindIP, bindPort)

while True:
    client, addr = server.accept()
    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

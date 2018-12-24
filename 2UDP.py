# coding=utf-8
import socket

targetHost = "127.0.0.1"
targetPort=80

#AF_INET nos refiere a ipv4
#SOCK_DGRAM nos refiere a UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Al ser UDP no existe método connct por lo que se manda el mensaje y el hos con el puert en la misma sencentcia
client.sendto("AAABBCC", (targetHost, targetPort))
#Obtenemos la respuesta data y detalles remotos: host y puerto
data, addr = client.recvfrom(4096)
print data

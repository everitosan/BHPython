import socket

targetHost="0.0.0.0"
targetPort=9999

#AF_INET nos refiere a usar ipv4
#SOCK_STREAM nos refiere a usar tcp
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((targetHost, targetPort))

client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(4096)
print response


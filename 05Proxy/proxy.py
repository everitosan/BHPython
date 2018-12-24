def receive_from(socket):
    buffer = ""
    reading = True
    socket.settimeout(1)
    try:
        while reading:
            data = socket.recv(4096)
            if not data:
                reading = False
            else:
                buffer += data
    except:
        pass
    return buffer


def request_handler(buffer):
    return buffer


def response_handler(buffer):
    return buffer

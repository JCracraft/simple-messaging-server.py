import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('0.0.0.0', 10000))
sock.listen(1)
connections = []

def handeler(c, a):
    global connections
    while True:
        data = c.recv(1024)
        for connection in connections:
            connection.send(byte(data))
            if not data:
                connections.remove(c)
                c.close()
                break

while True:
    c, a = socket.accept()
    cThread = threading.Thread(target=handeler, args=(c, a))
    cThread.daemon = True
    cThread.start()
    connections.append(c)
    print(connections)

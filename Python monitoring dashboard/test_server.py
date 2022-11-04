import socket
import json
from _thread import *

# Create a stream based socket(i.e, a TCP socket) operating on IPv4 addressing scheme
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
ThreadCount = 0

# Bind and listen
serverSocket.bind(("127.0.0.1",9090));
serverSocket.listen();

# Accept connections
while True:
    (clientConnected1, clientAddress) = serverSocket.accept();
    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));
    dataFromClient1 = clientConnected1.recv(1024)
    print(dataFromClient1.decode());
    data = json.loads(dataFromClient1.decode())


    (clientConnected2, clientAddress) = serverSocket.accept();
    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));
    dataFromClient2 = clientConnected2.recv(1024)
    print(dataFromClient2.decode());
    data = json.loads(dataFromClient2.decode())
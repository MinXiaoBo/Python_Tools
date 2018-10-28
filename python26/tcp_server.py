#!/usr/bin/python

import sys
import socket
import threading

bind_host = "127.0.0.1"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_host, bind_port))
server.listen(5)


def client_handler(client_socket):
    request = client_socket.recv(4096)
    print "[*] Recvied: %s" % request
    client_socket.send("ACK!")
    client_socket.close()


while True:
    client, addr = server.accept()
    print "[*] Accepted connect from %s:%d" % (addr[0], addr[1])
    client_handler = threading.Thread(target=client_handler, args=(client, ))
    client_handler.start()



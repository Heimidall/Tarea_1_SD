#!/usr/bin/python
import socket

skt = socket.socket()
skt.bind(('localhost',5000))
skt.listen(7)

archivo = open('log.txt', 'a')
cont = 7
flag = True
while flag:
    connection, address = skt.accept()

    Clientmessage = connection.recv(1024).decode()

    if Clientmessage:
        archivo.write(Clientmessage+' '+address[0]+'\n')
        connection.sendall('He recibido tu mensaje'.encode())
    connection.close()
    cont -=1
    if cont == 0:
        flag = False
archivo.close()

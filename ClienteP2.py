#!/usr/bin/python
import socket

# enviar mensajes al headnode
# recibir mensaje desde el headnode
# escribir en registro_cliente.txt el datanode que guarda mi mensaje

sock = socket.socket()
sock.connect(('localhost',5005))

registro = open('registro_cliente.txt','a')
cont = 1
flag = True
while flag:
    try:
        mensaje = 'mensaje número '+str(cont)+' desde el cliente'
        sock.sendall(mensaje.encode())

        data = sock.recv(1024).decode()
        registro.write(data+'\n')
        cont+=1
sock.close()
registro.close()

#!/usr/bin/python
import socket

# enviar mensajes al headnode
# recibir mensaje desde el headnode
# escribir en registro_cliente.txt el datanode que guarda mi mensaje

sock = socket.socket()
<<<<<<< HEAD:ClienteP2.py
sock.connect(('localhost',5004))
=======
sock.connect(('127.0.0.4',5004))
>>>>>>> 8067ab743a027741ff2bc2be4c374702b5422ebe:Ejercicio_2/ClienteP2.py

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
    except:
        c=0
sock.close()
registro.close()

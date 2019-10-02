#!/usr/bin/python
import socket

# enviar mensajes al headnode
# recibir mensaje desde el headnode
# escribir en registro_cliente.txt el datanode que guarda mi mensaje

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
print(ip)
sock.connect(('localhost',5004))

registro = open('registro_cliente.txt','a')
cont = 1
flag = True
while flag:
    try:
        print("Cliente: Try inicio")
        mensaje = 'mensaje número '+str(cont)+' desde el cliente'
        sock.sendall(mensaje.encode())
        print("Cliente: Try Despues de sendall")
        data = sock.recv(1024).decode()
        print("Cliente: data")
        registro.write(data+'\n')
        print("Cliente: Try inicio")
        cont+=1
    except:
        print("Cliente: Except")
        c=0
sock.close()
registro.close()

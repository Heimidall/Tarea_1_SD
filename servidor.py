#!/usr/bin/python

import socket
#import sys

# Creando el socket TCP/IP
sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#input direccion IP del Servidor y creacion de log.txt
#ipAddress = input('ingrese dirección ip del servidor: ')
archivo = open('log.txt', 'w')

# Enlace de socket y puerto
sockt.bind(('localhost',5000))

# Escuchando conexiones entrantes
sockt.listen(1)

flag = True
flag2 = True
while flag:
    # Esperando conexion
    connection, client_address = sockt.accept()

    try:
        # Recibe los datos en trozos y reetransmite
        while flag2:
            data = connection.recv(1024).decode() #recv(1024).decode() vercion de redes
            
            if data:
                archivo.write(data+' '+client_address[0]+'\n') 
                message = 'He recibido tu mensaje'
                connection.sendall(message.encode())
            else:
                #break
                flag2 = False          
    finally:
        # Cerrando conexion
        connection.close()
        archivo.close()
        flag=False
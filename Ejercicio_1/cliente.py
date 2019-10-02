#!/usr/bin/python

import socket
import sys
 
archivo = open('respuestas.txt','a')

# Creando un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Conecta el socket en el puerto cuando el servidor esté escuchando
#server_address = ('localhost', 5000)
sock.connect(('localhost', 5000))

#while flag=True:
try:
    # Enviando datos
    message = 'Saludos desde el cliente.'#message = input('ingrese mensaje para el servidor')
    sock.sendall(message.encode())#.enconde())

    # Buscando respuesta
    data = sock.recv(1024).decode()
    print ('respuesta del servidor: '+data)
    archivo.write(data+'\n')

finally:
    sock.close()
archivo.close()
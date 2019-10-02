#!/usr/bin/python
import socket
import struct
import sys

multicast_group = '224.10.10.10'
server_address = ('', 5000)

# Creae el socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = socket.gethostbyname(socket.gethostname())
# Enlazar el soket a la direccion del servidor
print(ip)
# Enlazar el soket a la direccion del servidor
sock.bind(server_address)

# Agregar el socket al grupo multicast
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)

# socket comunicacion 1 a 1
sckt = socket.socket()
sckt.connect(('127.0.0.3', 5003)) #deberia cambiar segun el nodo que sea entre [5001 - 5004]


# recibir multicast
# responder 'estoy vivo'
# recibir mensaje del cliente desde el headnode
# escribir ese mensaje en data.txt
# mandar 'registro fue correcto


# ciclo de recepcio y envio de mensajes
while True:
    # recibir multicast
    archivo = open('data.txt','a')
    data, address = sock.recvfrom(1024) # data = mensaje  adress = ('IP', puerto) del server
    # responder estoy vivo
    sock.sendto(b'Estoy vivo!', address) # respondemos el multicast
    try:  
        mensajeServer = sckt.recv(1024).decode() #recibir mensaje
        archivo.write(mensajeServer+'\n') #escribir en data.txt
        sckt.sendall('registro fue correto'.encode())
    except:
        c=0
    archivo.close()
sock.close()
sckt.close()

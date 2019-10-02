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
sock.bind(server_address)

# Agregar el socket al grupo multicast
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)

# socket comunicacion 1 a 1
#sckt = socket.socket()
#sckt.connect(('localhost', 5002)) #deberia cambiar segun el nodo que sea entre [5001 - 5004]


# recibir multicast
# responder 'estoy vivo'
# recibir mensaje del cliente desde el headnode
# escribir ese mensaje en data.txt
# mandar 'registro fue correcto


# ciclo de recepcio y envio de mensajes
while True:
    archivo = open('data.txt','a')
    # recibir multicast
    data, address = sock.recvfrom(1024) # data = mensaje  adress = ('IP', puerto) del server
    print("DataNode Mensaje recibido1: ", (data,address))
    # responder estoy vivo
    sock.sendto(b'Estoy vivo!', ('10.0.75.1',5000)) # respondemos el multicast
    print("DataNode Mensaje recibido2")
    try:  
        print("Datanode2 Try")
        mensajeServer , address= sock.recvfrom(1024)#recibir mensaje
        print("DataNode Mensaje recibido3", mensajeServer)
        mensajeServer = mensajeServer.split(' ')
        if mensajeServer[-1] == sock.gethostbyname(socket.gethostname()):
            archivo.write(mensajeServer+'\n') #escribir en data.txt
            sock.sendto(b'registro fue correto', address)
    except:
        print("DataNode Except")
        c=0
    archivo.close()
sock.close()


#!/usr/bin/python
import socket
import struct
import time
import random

message = b'estas vivo?'
multicast_group = ('224.10.10.10', 5000)

# Crear el socket multicast
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Asignar timeout para no boquear el socket al tratar de recivir datos
sock.settimeout(0.2)

# Asignar el TTL para que el mensaje solo pase por la red local
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# -------------------------------------------------------------------
# enviar multicast cada 5 segundos                                   ok 1
# escribir respuesta en hearbeat_server.txt                          ok 2 
# guardar mensajes del cliente                                       ok 3
# seleccionar un datanote aleatorio y                                ok 4
# mandarle el mensaje del cliente al nodo seleccionado                  5
# recibir mensaje del datanode con "registro correcto"                  6
# escribir en registro_server.txt el datanode que guarda el mendaje  ok 7
# mandar un mesaje al cliente con el datanode que recibio su mensaje ok 8
# -------------------------------------------------------------------


#socket del cliente
Clientsock = socket.socket()
Clientsock.bind(('localhost',5004))
Clientsock.listen(1)

hearbeat = open('hearbeat_server.txt','w')
registro = open('registro_server.txt','w')

while True: #loop infinito
    
    try:
        flag = True
        # Enviar mensaje multicast al grupo 1 
        sent = sock.sendto(message, multicast_group)
         
        while flag: # esperar respuestas del multicast
            #guardar mensaje del cliente 3
            ClientConn, ClientAdd = Clientsock.accept()
            ClientMessage = ClientConn.recv(1024).decode()
            
            IPRespuestas = list()
            
            try:
                data, server = sock.recvfrom(1024) #->data = respuesta. ->server = ('IP', puerto) del que responde
                IPRespuestas.append(server[0]) #guarda las ips de lo que respondieron
            except socket.timeout:
                # la respuesta no llega ates del timeout
                flag = False
                #break
            else: # si hay respuestas antes del timeout
                
                hearbeat.write(data+' desde'+server[0]+'\n') # escribir respuesta en hearbeat_server.txt 2 
                
                elegido = random.choice(IPRespuestas) # elegir un nodo random, mandarle del ClientMessage 4
                
                #mandar el mensaje a todos
                sock.sendto(ClientMessage+' '+elegido, multicast_group)

                ClientConn.sendall(elegido.encode()) # mandarle el mensaje del cliente al nodo seleccionado
                
                
                # recibir mensaje del datanode con "registro correcto"
                registro.write(elegido.encode()+'\n')   # escribir en registro_server.txt el datanode que fuarda el mensaje 7
                ClientConn.sendall(elegido.encode()) # mandar un mesaje al cliente con el datanode que recibio su mensaje 8
            flag = True
            time.sleep(5) #esperar 5 segundos 1 
            sent = sock.sendto(message, multicast_group) #mandar multicast 1 

    except:
        c=0
    
sock.close()
Clientsock.close()
nodo1.close()
nodo2.close()
nodo3.close()
hearbeat.close()
registro.close()
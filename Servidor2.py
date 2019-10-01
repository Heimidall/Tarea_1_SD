#!/usr/bin/python
'''import socket
#HEADNODE
# se crean los socket para cada conexion
skt1 = socket.socket()
skt1.bind(('localhost',5001))
skt1.listen(1)

skt2 = socket.socket()
skt2.bind(('localhost',5002))
skt2.listen(1)

skt3 = socket.socket()
skt3.bind(('localhost',5003))
skt3.listen(1)

skt4 = socket.socket()
skt4.bind(('localhost',5004))
skt4.listen(1)

connection1, address1 = skt1.accept() #datanode1
connection2, address2 = skt2.accept() #datanode2
connection3, address3 = skt3.accept() #datanode3
connection4, address4 = skt4.accept() #container cliente

MulticastMessage = b"estás vivo?"

archivo = open('log.txt', 'a')
cont = 7
flag = True
while flag:'''
    # enviar multicast cada 5 segundos
    # escribir respuesta en hearbeat_server.txt
    # guardar mensajes del cliente
    # seleccionar un datanote aleatorio y mandarle el mensaje del cliente
    # recibir mensaje del datanode con "registro correcto"
    # escribir en registro_server.txt el datanode que se selecciona
    # mandar un mesaje al cliente con el datanode que recibio su mensaje

'''
    Clientmessage1 = connection1.recv(1024).decode()

    if Clientmessage1:
        archivo.write(Clientmessage1+' '+address1[0]+'\n')
        connection1.sendall('He recibido tu mensaje'.encode())
    connection1.close()
    cont -=1
    if cont == 0:
        flag = False'''
#archivo.close()

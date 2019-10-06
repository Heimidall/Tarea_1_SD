import socket
import struct
import time
import random
import threading
message = b'Estas vivo?'
multicast_group = ('224.10.10.10', 10000)
server_address = ('0.0.0.0', 9999)

print('Starting up on {} port {}'.format(*server_address))

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
sock.settimeout(15)

# Set the time-to-live for messages to 1 so they do not
# go past the local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)


#Crear socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.bind(server_address)
cliente.listen(10)
timer = None
def multicast_Message():
    global timer
    sent = sock.sendto(message, multicast_group)
    data , server = sock.recvfrom(1024)
    mensaje = 'Recibiendo {!r} desde {} \n'.format(data.decode(), server)
    print(mensaje)
    hearbeat = open('hearbeat_server.txt','a')
    hearbeat.write(mensaje) # escribir respuesta en hearbeat_server.txt 2 
    hearbeat.close()
    timer = threading.Timer(5,multicast_Message)
    timer.start()

flag = True
#timer = threading.Timer(5,multi_mensaje,[message])
timer = threading.Timer(5,multicast_Message)
timer.start()
connection, address = cliente.accept()
while True:
    Clientmessage = connection.recv(1024).decode()
    if Clientmessage:
        elegido = random.choice([1,2,3])
        if elegido == 1:
            mensajecliente = (Clientmessage + '1').encode()
        elif elegido == 2:
            mensajecliente = (Clientmessage + '2').encode()
        elif elegido == 3:
            mensajecliente = (Clientmessage + '3').encode()
        print("HEADNODE: ENVIO UN MENSAJE DEL CLIENTE A LOS DATANODES")
        sent = sock.sendto(mensajecliente, multicast_group)
        data , server = sock.recvfrom(1024)
        if data:
            data = data.decode()
            if data == 'Registro fue correcto':
                mensaje = ('Su mensaje fue guardado en el datanode ' + str(elegido)).encode()
                connection.sendall(mensaje)
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
cliente.listen()
timer = None
def multicast_Message():
    global timer
    sent = sock.sendto(message, multicast_group)
    data , server = sock.recvfrom(1024)
    mensaje = 'Recibiendo {!r} desde {} \n'.format(data, server)
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
while True:
    try:
        connection, client_address = cliente.accept()
        # Send data to the multicast group
        print('sending {!r}'.format(message))
        sent = sock.sendto(message, multicast_group)
        # Look for responses from all recipients
        while True:
            print('waiting to receive')
            try:
                data_cliente = connection.recv(1024)
                msj_cliente = data_cliente.decode()
                print("Mensaje de vuelta al cliente")
                elegido = random.choice([1,2,3])
                if elegido == 1:
                    mensajecliente = (msj_cliente + '1').encode()
                elif elegido == 2:
                    mensajecliente = (msj_cliente + '2').encode()
                elif elegido == 3:
                    mensajecliente = (msj_cliente + '3').encode()
                sent2 = sock.sendto(mensajecliente,multicast_group)
                if data_cliente:
                    connection.sendall(data_cliente)
                data2, server2 = sock.recvfrom(16)
                mensaje2 = data2.decode()
                if mensaje2 == 'Registro fue correcto': #deberia mandar al clientre
                    msj = ("El mensaje fue guardado en el data node" + elegido).encode()
                    connection.sendall(msj)
                else:
                    print(mensaje2)
                break
            except:
                socket.timeout
                print('No hay mas mensajes, cerrando socket')
                flag = False
                break
    except:
        print("No se pudo establecer comunicacion")
    
print('closing socket')
sock.close()
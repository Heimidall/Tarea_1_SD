import socket
import struct
import time
message = b'Estas vivo?'
multicast_group = ('224.10.10.10', 10000)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
sock.settimeout(15)

# Set the time-to-live for messages to 1 so they do not
# go past the local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

flag = True
while True:
    try:
        hearbeat = open('hearbeat_server.txt','a')
        # Send data to the multicast group
        print('sending {!r}'.format(message))
        sent = sock.sendto(message, multicast_group)
        print("entre al try")
        # Look for responses from all recipients
        while True:
            print('waiting to receive')
            try:
                data, server = sock.recvfrom(16)
                mensaje = 'Recibiendo {!r} desde {} \n'.format(data, server)
                print(mensaje)
                #sent = sock.sendto(message, multicast_group)
                hearbeat.write(mensaje) # escribir respuesta en hearbeat_server.txt 2 
                print('received {!r} from {}'.format(data, server))
                sent2 = sock.sendto(b'Mensaje cliente',multicast_group)
                print('sent2 \n')
                break
            except:
                socket.timeout
                print('No hay mas mensajes, cerrando socket')
                flag = False
                break
        time.sleep(5) #esperar 5 segundos 1
    except:
        print("No se pudo establecer comunicacion")
    
print('closing socket')
hearbeat.close()
sock.close()
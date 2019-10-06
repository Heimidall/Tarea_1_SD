import socket
import struct
import sys

multicast_group = '224.10.10.10'
server_address = ('', 10000)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the server address
sock.bind(server_address)

# Tell the operating system to add the socket to
# the multicast group on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    mreq)

ID = '3'
# Receive/respond loop
while True:
    print('Esperando mensajes \n')

    data, address = sock.recvfrom(1024) #consulta del HEadNode
    if data:
        data = data.decode()
        print("El mensaje que le llega al datanode3 es:", data)
        if data == 'Estas vivo?':
            print('Data Node 3 vivo', address)
            sock.sendto(b'Data Node 3 vivo', address)
        else:
            datos = data.split(' ')
            if datos[-1] == ID:
                archivo = open('data.txt' ,'a')
                archivo.write(data+'\n')
                archivo.close()
                sock.sendto(b'Registro fue correcto',address)
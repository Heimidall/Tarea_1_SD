import socket
import time
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('0.0.0.0', 9999)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
try:
    # Send data
    message = b'Este es un mensaje del cliente que va para el data node '
    sock.sendall(message)
    print("\n CLIENTE ENVIA EL PRIMER MENSAJE:", message)
    while True:
        data = sock.recv(1024)
        if data:
            data = data.decode()
            print("CLIENTE: El mensaje que recibo es ", data)
            registro = open('registro_cliente.txt','a')
            registro.write(data+'\n')
            registro.close()

            sock.sendall(message)
            print("Envié un segundo mensaje \n")
        #print("EL CLIENTE RECIBIÓ DATOS \n")
        #print('received {!r}'.format(data))
        #print('client escribe')

finally:
    print('closing socket')
    sock.close()
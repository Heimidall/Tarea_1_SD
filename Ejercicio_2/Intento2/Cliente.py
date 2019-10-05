import socket
import time
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 9999)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message = b'Este es un mensaje del cliente que va para el data node '
    print('sending {!r}'.format(message))
    while True:
        sock.sendall(message)
        #time.sleep(5)
        data = sock.recv(1024)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
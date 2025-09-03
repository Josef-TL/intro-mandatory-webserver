from socket import *
import andreas
import josef
import lykke

server_port = 80
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)

print("The server is ready to receive.")
while True:
    connection_socket, addr = server_socket.accept()
    msg = connection_socket.recv(2048).decode()

    # Herfra skal vi bearbejde http request
    print("Received message:", msg)
    connection_socket.send("Response")
    connection_socket.close()
    

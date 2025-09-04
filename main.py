from socket import *
import andreas
import josef
import lykke

server_port = 15000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)

print("The server is ready to receive.")
while True:
    connection_socket, addr = server_socket.accept()
    msg = connection_socket.recv(2048).decode()

    # Herfra skal vi bearbejde http request
    result = andreas.handle_request(connection_socket, msg)

    # Når vi har modtaget og bearbedet en request, 
    # skal resultatet være en liste af strings, med hver linje af requesten som en item
    print("Received message:", msg)

    ###########
    ## Her laver jeg respose shit
    # funktionen tager url og status code som input
    # og returnerer en string med hele response og byte-længden af body
    res, body_len = josef.create_response("/",200)

    ###########

    connection_socket.send(res.encode())
    connection_socket.close()
    

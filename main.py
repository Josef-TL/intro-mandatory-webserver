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
    print("Raw request:\n", msg)

    # Default response values
    status = 500
    url = "/"

    # Step 1: Parse the request with andreas.py
    result = andreas.handle_reques(msg)

    # We need to save the "status" and "url" values that andreas.handle_request(msg) returns,
    # so that we can pass them to josef.create_response(url,status) as parameters 
    if result["status"] == 200:
        url = result["path"]      # "/index" or "/test"
        status = 200
    elif result["status"] == 400:
        status = 400
    else:
        status = 500

    # Step 2: Build response with josef.py
    res, body_len = josef.create_response("/",200)

    # Step 3: Send response back
    connection_socket.send(res.encode())
    connection_socket.close()
    

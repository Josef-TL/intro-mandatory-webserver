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

    # Step 1: Parse the request with andreas.py
    result = andreas.handle_request(msg)

    # We need to save the "status" and "url" values that andreas.handle_request(msg) returns,
    # so that we can pass them to josef.create_response(url,status) as parameters 
    status = result.get("status", 500)
    url = result.get("path", "")
    method = result.get("method", "")
    version = result.get("version", "")
    error_msg = result.get("body", "")

    # Step 2: Build response with josef.py
    res, body_len, status, error_msg = josef.create_response(url,status,error_msg)

    # Step 3: Send response back
    connection_socket.send(res.encode())
    connection_socket.close()

    # Step 4: Log the request in Apache format
    client_ip = addr[0]
    lykke.log_request(client_ip, method, url, version, status, body_len, error_msg)
    

from socket import *
import response_builder
import request_handler
import log

server_port = 15000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)

print("The server is ready to receive.")

while True:
    connection_socket, addr = server_socket.accept()
    request = connection_socket.recv(1024).decode()
    print("Request received:\n", request)

    try:
        # Determine requested file
        filename = request_handler.parse_request(request)

        # Try to open the file
        try:
            with open(filename + ".html", "r") as f:
                body = f.read()
                """
                Python will look for the file in the current working directory, 
                i.e., the folder where we started main.py in our terminal.
                The client will then see the body of the html file in the browser 
                (the website will open)
                """
            response = response_builder.build_response(200, body)

        except FileNotFoundError:
            # If file is missing, send 404 Not Found
            response = response_builder.build_response(404, "<h1>404 Not Found</h1>")

    except ValueError:
        # Malformed request → 400 Bad Request
        response = response_builder.build_response(400, "<h1>400 Bad Request</h1>")
    except Exception as e:
        # Catch-all for unexpected errors → 500
        response = response_builder.build_response(500, f"<h1>500 Internal Server Error</h1><p>{e}</p>")

    connection_socket.send(response.encode())
    connection_socket.close()
    
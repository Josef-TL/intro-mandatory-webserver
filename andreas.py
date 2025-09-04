from socket import * 

def handle_request(connection_socket, msg):
    try:
        # 1. Læser requesten 
        lines = msg.split("\r\n") 
        if not lines or not lines[0]:
            connection_socket.close()
            return
        print("Request lines:", lines) 

        # 2. Parse første linje
        try:
            method, path, version = lines[0].split()
        except ValueError:
            return {"status": "400 Bad Request", "body": "Bad Request"}
    
        # 3. Tjek om det er en gyldig HTTP/1.1 GET request
        if method != "GET" and path != "/" and version != "HTTP/1.1":
            return {"status": "400 Bad Request", "body": "Bad Request"} 
        
        # 4. Returner en simpel response
        return {"status": 200, "method": method, "path": path, "version": version}
    
    except Exception as e:
        return {"status": 500, "reason": str(e)}

"""
The purpose of andreas.py should just be:

1. Parse the incoming request.

2. Validate it.

3. Return structured data (method, path, version, maybe an error code).

Then main.py decides what to do with that data (e.g. call josef.py to build the response).
"""

def handle_request(msg):
    try:
        # 1. splitter requesten 
        lines = msg.split("\r\n") 
        if not lines or not lines[0]:
            return {"status": 400, "body": "Bad Request"}

        # 2. Parse første linje
        try:
            method, path, version = lines[0].split()
        except ValueError:
            return {"status": 400, "body": "Bad Request"}
    
        # 3. validerer at det er en gyldig HTTP/1.1 GET request
        if method != "GET" or version != "HTTP/1.1":
            return {"status": "400 Bad Request", "body": "Bad Request"} 
        
        # 4. Returner en simpel response
        return {"status": 200, "method": method, "path": path, "version": version}
    
    except Exception as e:
        return {"status": 500, "reason": str(e)}

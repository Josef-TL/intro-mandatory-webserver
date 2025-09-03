def parse_request(request: str) -> str:
    # Parsing means turning raw text from the request into an organized list of instructions

    """
    Parses the HTTP request and returns the requested html-file path.
    Raises ValueError if the request is malformed.
    """

    try:
        parts = request.split() # returns a list

        # A valid request should start with: METHOD PATH HTTP/VERSION
        # METHOD has to be GET and the request has to be at least 3 parts long 
        if len(parts) < 3 or not parts[0].startswith("GET"):
            raise ValueError("Malformed HTTP request")

        path = parts[1]
        if path == "/":
            return "index"
            # The server uses the string find the html-file in the repository 
            # and opens the file for the client
        else:
            return path.lstrip("/")  
            # removes leading "/" and returns the name of the file that the client requested

    except Exception as e:
        raise ValueError("Bad Request") from e

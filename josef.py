# Jeg skal lave noget funktionalitet der laver et response
def create_response(url, status):
    status_codes = {200: "OK",
                    404: "Not Found",
                    500: "Internal Server Error",
                    501: "Not Implemented"}
    
  
    # her starter response. Vi kører altid med http v1.1
    res_head = "HTTP/1.1 "
    res_body = ""

    # sørger for at path er i den rigtige format.
    if url == "/":
        filename = "index.html"
    elif url.endswith(".html"):
        filename = url.lstrip("/")  # strip leading "/"
    else:
        filename = url.lstrip("/") + ".html"

    # Prøv at åbne filen. Hvis man kan, kør videre
    #  hvis det fejler med 404, lav status om
    try:
        with open(filename, "r") as f:
            res_body = f.read()

        # Laver response header. Vi kører altid med http v1.1
        # checker status koden og laver header derudfra.
        
        if status in status_codes:
            res_head += str(status) + " " + status_codes[status] + "\r\n"
        
        else:
            res_head += "500 " + status_codes[500] + "\r\n"
            status = 500
        
    except FileNotFoundError:
        res_body = "<html><h1>404 Not Found</h1></html>"
        res_head += "404 " + status_codes[404] + "\r\n"
        status = 404
        

    
    # slutter header
    res_head += "\r\n"

    # checker body lenght for logging purpose
    body_len = len(res_body.encode("utf-8"))

    return res_head + res_body, body_len, status
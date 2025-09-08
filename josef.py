# Jeg skal lave noget funktionalitet der laver et response
def create_response(url, status, error_msg):
    status_codes = {200: "OK",
                    400: "Bad request",
                    404: "Not Found",
                    500: "Internal Server Error"}
    
  
    # her starter response. Vi kører altid med http v1.1
    res_head = "HTTP/1.1 "
    res_body = ""

    

    # sørger for at path er i den rigtige format.
    while True:
        if url == "":
            break
        elif url == "/":
            filename = "index.html"
            break
        elif url.endswith(".html"):
            filename = url.lstrip("/")  # strip leading "/"
            break
        else:
            filename = url.lstrip("/") + ".html"
            break


    # checker status
    match status:
        case 200:
            # Prøv at åbne filen. Hvis man kan, kør videre
            # hvis det fejler med 404, lav status om 
            try:
                with open(filename, "r") as f:
                    res_body = f.read()
                res_head += str(status) + " " + status_codes[status] + "\r\n"

            except FileNotFoundError:
                status = 404
                error_msg = status_codes[status]
                res_body = "<html><h1>404 Not Found</h1></html>"
                res_head += str(status) + status_codes[status] + "\r\n"
                
        # Manuel html
        case 400:
            res_body = "<html><h1>400 Bad request</h1></html>"
            res_head += str(status) + " " + status_codes[status] + "\r\n"

        case 500:
            res_body = "<html><h1>500 Internal server error</h1></html>"
            res_head += str(status) + " " + status_codes[status] + "\r\n"


    # slutter header
    res_head += "\r\n"

    # checker body lenght for logging purpose
    body_len = len(res_body.encode("utf-8"))

    return res_head + res_body, body_len, status, error_msg
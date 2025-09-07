# Jeg skal lave noget funktionalitet der laver et response
def create_response(url, status):
    status_codes = {200: "OK",
                    404: "Not Found",
                    500: "Internal Server Error",
                    501: "Not Implemented"}

    res_head = "HTTP/1.1 "
    if status in status_codes:
        res_head += str(status) + " " + status_codes[status] + "\r\n"

    res_head += "\r\n"
    res_body = ""

    
    match url:
        case "/":
            with open("index.html", "r") as f:
                res_body += f.read()
        case "/index":
            with open("index.html", "r") as f:
                res_body += f.read()
        case "/test":
            with open("test.html", "r") as f:
                res_body += f.read()
        case _:
            res_body += "<html><h1>404 Not Found</h1></html>"

    body_len = len(res_body.encode("utf-8"))
    return res_head + res_body, body_len
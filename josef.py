# Jeg skal lave noget funktionalitet der laver et response
def create_response(request_lines, status):
    res = ["HTTP/1.1",str(status)+" OK"] 
    res.append("asd")
    res = " ".join(res)
    return res

print(create_response_header(2,200))
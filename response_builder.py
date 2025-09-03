def build_response(status_code: int, body: str, content_type="text/html") -> str:
    status_text = {
        200: "OK",
        400: "Bad Request",
        404: "Not Found",
        500: "Internal Server Error"
    }.get(status_code, "Unknown")

    response = f"HTTP/1.1 {status_code} {status_text}\r\n"
    response += f"Content-Type: {content_type}\r\n"
    response += f"Content-Length: {len(body.encode())}\r\n"
    response += "\r\n"
    response += body
    return response


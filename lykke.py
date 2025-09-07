import datetime

"""
1. Logs every request after sending a response.
2. Uses Apache-style format with:
    Client IP
    Timestamp
    HTTP method + path + version
    Status code
    Response size in bytes
3. Keeps old logs because it opens the file in append mode.
"""

LOGFILE = "server.log"

def log_request(ip, method, path, version, status, size):
    """
    Logs an HTTP request in Apache format.
    Example:
    127.0.0.1 - - [07/Sep/2025:15:30:22 +0000] "GET /index.html HTTP/1.1" 200 17
    """
    # Gets the datetime and formats it to APACHE format
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%d/%b/%Y:%H:%M:%S +0000")
    # Creates f-string with the arguments in APACHE format
    entry = f'{ip} - - [{now}] "{method} {path} {version}" {status} {size}\n'
    
    # Logs entry(the http request) in server.log
    # Also creates ther server.log file if it doesnt exist
    with open(LOGFILE, "a") as f:  # append mode
        f.write(entry)

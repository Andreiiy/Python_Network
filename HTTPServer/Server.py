
from socket import  *

#region------------  C O N S T A N T S ----------------------------
PORT=9080                 #
IP=""
ADDR = (IP,PORT)
BUF_SIZE = 2000
VERSION = "HTTP/1.1"
STATUS_OK = "200 OK"
ENDLINE = "\r\n"
#endregion

#region------------  G L O B A L S ----------------------------
sockListen = None
#endregion

#region------------  M E T H O D S ----------------------------
def listen():
    global sockListen
    sockListen = socket()
    sockListen.bind(ADDR)
    sockListen.listen(1)
    print  "Server waiting..."


def get_file_content(filename):
    file_index = open(filename, "rb")
    file_content = file_index.read()
    file_index.close()
    return file_content

def response(data):
    response_data = ""
    headers_items = data.split(ENDLINE)
    if headers_items[0].startswith("GET"):
        url = headers_items[0].split(" ")[1]
        response_data = VERSION + " " + STATUS_OK + ENDLINE + ENDLINE
        if url == "/":
            file_content = get_file_content("index.html")
        else:
            file_content = get_file_content(url[1:])

    return response_data+file_content

    return  response_data

def request_response():
    global sockListen
    exit = False
    while True:
        sock, addr = sockListen.accept()
        try:
            request_data = sock.recv(BUF_SIZE)
            print "Client : ", addr[0]
            print request_data
            if request_data and len(request_data) > 0 :
                response_data = response(request_data)
                sock.send(response_data)
                sock.close()
        except error as er:
            exit = True
#endregion

#region------------  M A I N  ----------------------------
def main():
    listen()
    request_response()
#endregion

if  __name__== "__main__":
    main()


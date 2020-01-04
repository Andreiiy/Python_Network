import socket
from Security import *
import ssl

security = Security("qwertyuiop")

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0',8820))
server_socket.listen(1)
client_sock, adr = server_socket.accept()

go = True
name_client = client_sock.recv(1024)
print "Helo my name is "+name_client
name= raw_input("Enter Name")
client_sock.send(name)

while go:
    data= security.decrypt( client_sock.recv(1024) )
    if data == "bye":
        go = False
        server_socket.close()
        client_sock.close()
    else:
        print name_client +":"+data
        msg = raw_input(name +':')
        client_sock.send( security.encrypt(msg) )



import socket

server_socket=socket.socket()
server_socket.bind(('0.0.0.0',8820))
server_socket.listen(1)
client_sock, adr = server_socket.accept()

go = True
name_client = client_sock.recv(1024)
print "Helo my name is "+name_client
name= raw_input("Enter Name")
client_sock.send(name)

while go:
    data=client_sock.recv(1024)
    if data == "bye":
        go = False
        server_socket.close()
        client_sock.close()
    else:
        print name_client +":"+data
        msg = raw_input(name +':')
        client_sock.send(msg)



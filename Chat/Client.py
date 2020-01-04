import socket

cli_socket = socket.socket()
cli_socket.connect(('127.0.0.1',8820))

go = True
name= raw_input("Enter Name")
cli_socket.send(name)
name_serv = cli_socket.recv(1024)
print "Helo my name is "+name_serv

while go:
    msg = raw_input(name +':')
    cli_socket.send(msg)

    if msg == "bye":
        go = False
        cli_socket.close()
    else:
        data=cli_socket.recv(1024)
        print name_serv +":"+data





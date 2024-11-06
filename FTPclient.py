import socket

host="127.0.0.1"
port=1020
s=socket.socket()
s.connect((host,port))

filename=input(str("ENetr file name:"))
file=open(filename,'wb')

filedata=s.recv(1024)
file.write(filedata)
file.close()

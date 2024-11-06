import socket

host="127.0.0.1"
port=1020
s=socket.socket()
s.bind((host,port))
s.listen(1)

conn,addr=s.accept()

filename=input(str("ENetr file name:"))
file=open(filename,'rb')

file_data=file.read(1024)
conn.send(file_data)



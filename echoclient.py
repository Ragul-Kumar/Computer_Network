import socket
port=1030
host='127.0.0.1'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))

str = "HI"
data=str.encode('utf8')
s.send(data)
data=s.recv(1024)
s.close()
print(data)
import socket
port=1030
host='127.0.0.1'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn,addr=s.accept()
while 1:
    data=conn.recv(1024)
    print(data)
    if not data:
        break
    conn.send(data)
s.close()
    
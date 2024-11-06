import socket

def Server_socket():
    host='127.0.0.1'
    port=1020
    s=socket.socket()
    s.bind((host,port))
    s.listen(2)
    conn,addr=s.accept()
    print("address",addr)

    while True:
        data=conn.recv(1024).decode()
        if not data:
            break
        print("message",data)
        data=input("->")
        conn.send(data.encode())
    s.close()

Server_socket()
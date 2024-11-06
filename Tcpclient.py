import socket

def client_server():
    print("Bye to teriminate.")
    host="127.0.0.1"
    port=1020
    s=socket.socket()
    s.connect((host,port))

    message=input("->")

    while message.lower().strip() != 'bye':
        s.send(message.encode())
        data=s.recv(1024).decode()
        print(data)
        message=input("->")
    s.close()

client_server()
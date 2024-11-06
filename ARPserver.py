import socket

UPD_IP='127.0.0.1'
UDP_PORT=1020
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
Message='127.90.3.56'
s.sendto(bytes(Message,('utf-8')),(UPD_IP,UDP_PORT))
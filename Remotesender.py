import socket

UDP_IP='127.0.0.1'
UDP_PORT=1020
MESSAGE='notepad'
print('message',MESSAGE)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(bytes(MESSAGE,"utf-8"),(UDP_IP,UDP_PORT))
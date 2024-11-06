import socket

UDP_IP='127.0.0.1'
UDP_PORT=1020
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((UDP_IP,UDP_PORT))

ip=[ '1.11.1.1','127.90.3.56']
mac=['120','450']

while True:
    data,addr=s.recvfrom(1024)
    str=data.decode('utf-8')

    l=len(data)

    if l !=0:
        print(str)
        break
for x in ip:
    if str in ip:
        ind=ip.index(str)
        print(ind)

print("MAcaddres",mac[ind])

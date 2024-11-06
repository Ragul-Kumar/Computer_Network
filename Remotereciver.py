import socket
import wmi

UDP_IP='127.0.0.1'
UDP_PORT=1020
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((UDP_IP,UDP_PORT))
data,addr=s.recvfrom(1024)
data=data.decode('utf-8')
print("MEssage",data)
print("Opening",data)

conn=wmi.WMI()
pid,returnval=conn.Win32_Process.Create(CommandLine=str)


from socket import *

socked=socket(AF_INET,SOCK_DGRAM)

socked.bind(("127.0.0.1",8888))

while True:
    data,addr=socked.recvfrom(1024)
    print("收到信息为：",data.decode())
    socked.sendto(b"Thanks",addr)

socked.close()

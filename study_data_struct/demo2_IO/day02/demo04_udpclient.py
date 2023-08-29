from socket import *

#服务端地址
ADDR=("127.0.0.1",8888)

socked=socket(AF_INET,SOCK_DGRAM)

while True:
    data=input("Msg>>>").encode()
    if not data:
        break
    socked.sendto(data,ADDR)

    data,addr=socked.recvfrom(1024)
    print(data.decode())

socked.close()

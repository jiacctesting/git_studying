from socket import *
from time import sleep

dest=("192.168.88.255",8999)

s=socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

data="哈哈哈哈哈"
while True:
    sleep(2)
    s.sendto(data.encode(),dest)


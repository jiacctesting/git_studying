"""
1：搭建网络
2：
"""
from socket import *
ADDR=('0.0.0.0',8889)
#存储用户信息格式{name:address}
user={}

def do_login(s,name,addr):
    if name in user:
        s.sendto("该用户已存在".encode(),addr)
        return
    s.sendto("OK".encode(),addr)
    #先通知其他人
    msg="欢迎'%s' 进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name]=addr #保留用户信息

def do_request(s):
    while True:
        data,addr=s.recvfrom(1024)
        tmp=data.decode().split(" ")[0]
        if tmp=="L":
            do_login(s,data.decode().split(" ")[1],addr)


def main():
    s=socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    do_request(s)

main()
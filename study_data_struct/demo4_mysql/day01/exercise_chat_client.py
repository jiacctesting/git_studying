from socket import *
ADDR=('127.0.0.1',8889)


def main():
    s=socket(AF_INET,SOCK_DGRAM)
    while True:
        name=input("请输入姓名")
        #定义协议中L代表登录请求，类似get post
        msg="L "+name
        s.sendto(msg.encode(),ADDR)
        #接收反馈
        data,addr=s.recvfrom(1024)
        #定义协议，返回OK就是允许
        if data.decode()=="OK":
            print("您已进入聊天室")
            break
        else:
            print("请重新输入姓名")

main()
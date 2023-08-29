with open(r"C:\Users\Lenovo\Desktop\test2.txt","rb+" ) as f:
    content=f.readlines()

from socket import socket

#创建套接字
sockfd=socket()

#连接
server_add=("127.0.0.1",8888)
sockfd.connect(server_add)

#发送接收
while True:
    with open(r"C:\Users\Lenovo\Desktop\test2.txt", "rb+") as f:
        data = f.read()
        sockfd.send(data)

    data=sockfd.recv(1024)
    print("Server:",data.decode())
    break

#关闭
sockfd.close()



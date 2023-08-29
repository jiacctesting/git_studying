from socket import socket

#创建套接字
sockfd=socket()

#连接
server_add=("127.0.0.1",8888)
sockfd.connect(server_add)

#发送接收
while True:
    data=input("Msg>>>")
    if not data:
        break
    sockfd.send(data.encode())
    data=sockfd.recv(1024)
    print("Server:",data.decode())

#关闭
sockfd.close()



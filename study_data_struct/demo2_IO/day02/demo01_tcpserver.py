import socket

#创建tcp套接字
sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
sockfd.bind(("127.0.0.1",8888))

#设置监听
sockfd.listen(5)

#阻塞等待处理连接
while True:
    print("waitting for connecting")
    connfd,addr=sockfd.accept()
    print("conncted ：" ,addr)

    #收发消息
    while True:
        data=connfd.recv(1024)
        if not data:#执行这条语句时，不是因为客户端输入为空，而是因为客户端输入为空导致break，从而造成服务端接收到的消息为空
            break
        print("收到消息:",data.decode())
        n=connfd.send(b'Thanks')
        print("发送%d字节"%n)

    #关闭套接字
    connfd.close()

sockfd.close()
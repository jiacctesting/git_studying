from socket import *

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(("127.0.0.1",8000))

s.listen(5)

while True:
    print("Waitting for connect-----")
    c,addr=s.accept()
    print("Connected by ",addr)
    data=c.recv(1024)
    print("收到请求为：",data)
    response="""HTTP/1.1 200 OK
    Content-Type:test/html

    hello world
    """
    c.send(response.encode())
    # c.send("HELLO".encode())
    print("Success")
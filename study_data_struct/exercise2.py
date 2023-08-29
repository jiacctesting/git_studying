from socket import *

socked=socket()

socked.connect(("127.0.0.1",8888))
socked.send(input("Msg:===").encode())
data=socked.recv(1024)
print("收到信息为：",data.decode())

socked.close()

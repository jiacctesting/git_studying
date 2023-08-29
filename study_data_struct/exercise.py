from socket import *

socked=socket()

socked.bind(("127.0.0.1",8888))

socked.listen()

print("waitting connect")
confed,addr=socked.accept()
print("连接成功，",addr)

data=confed.recv(1024)
print("接收信息为",data.decode())
confed.send(b"Thanks")

socked.close()
confed.close()


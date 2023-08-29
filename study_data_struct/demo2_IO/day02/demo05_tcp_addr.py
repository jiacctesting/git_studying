import socket
from socket import *
s=socket()
print("地址类型：",s.family)
print("套接字类型：",s.type)

#设置连接断开后端口可以立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("127.0.0.1",8888))
print("获取绑定地址",s.getsockname())

print("文件描述符",s.fileno())

s.listen(5)

c,addr=s.accept()

#连接套接字c 才可以调用，（所以必须要先有地址连接后才可以）结果与调用accept（）返回的addr一致
print("连接段地址：",c.getpeername())



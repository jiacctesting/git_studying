from socket import *

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(("127.0.0.1",8000))

s.listen(5)
# response_test="""GET / HTTP/1.1
#     Content-Type:test/html
#
#     hello world
#     """
def response(c):
    re=c.recv(1024)

    if not re:
        return
    request_line=re.decode().split("\n")[0]
    info=request_line.split(" ")[1]
    print(info)
    if info=="/":
        print("正确")
        with open("./index.html","r") as f:
            # response="""HTTP/1.1 200 OK
            # Content-Type:test/html
            #
            # """
            response = "HTTP/1.1 200 OK\r\n"
            response+="   Content-Type:test/html\r\n"
            response+=" \r\n"
            response+=f.read()
            print(response)
            # return response.encode()
    else:
        print("不正确")
        response = """HTTP/1.1 404 Not Fund
            Content-Type:test/html

            """
        # response = "HTTP/1.1 200 OK\r\n"
        # response += "Content-Type:test/html\r\n"
        # response += "\r\n"
        response += "<h1>Sorry....</h1>"
        print(response)

        # return response.encode()
    c.send(response.encode())

while True:
    c,addr=s.accept()
    print("Connected by ",addr)
    # data=c.recv(1024)
    # print("收到请求为：",data)
    response(c)
    # if not data:
    #     continue
    # response_data=response(data)
    # print(response_data)
    # c.send(response_data)
    # # c.send("HELLO".encode())
    # print("Success")

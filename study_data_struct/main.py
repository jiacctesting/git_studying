def func01(val):
    re=1
    while val>1:
        re*=val
        val=val-1

    return re
a=func01(4)
print(a)

def func02(num):
    if num<=1:
        return num
    return num*func01(num-1)
print(func02(5))

s="哈哈哈好开心"
a=list(s)
print(a.index("开"))

response="""HTTP/1.1 200 OK
    Content-Type:test/html

    hello world
    """
print(response.split(" ")[1])

a="我是是我"
if a[:]==a[::-1]:
    print("回文")

import os
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))
class Cas:
    B=1
    def print_a(self):
        return Cas.B
        # print(self.a)
m=Cas()
n=m.print_a()
print(n)
print("============")
a={1:2,3:4,4:5}
for k in a.values():
    print(k)

data = [2, 3, 6, 9, 2, 8]
data_ = [x if x > 5 else 0 for x in data]   
print(data_)
print("============")

def new_func(func):
    def wrapper(*args,**kwargs):
        print("装饰器")
        return func(*args,**kwargs)
    return wrapper

@new_func
def old_func(a):

    return a+1

m=old_func(10)
print(m)

current=os.path.abspath(__file__)
BASE_DIR=os.path.dirname(os.path.dirname(current))
print(current)
print(BASE_DIR)
print(os.path.dirname(os.path.dirname(__file__)))

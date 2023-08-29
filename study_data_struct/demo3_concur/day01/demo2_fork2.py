
import os
from time import sleep

print("===========")
a=1
#创建子进程
pid = os.fork()

if pid<0:
    print("the process failed")

#子进程执行部分
elif pid==0:
    print("the process is new")
    #打印：1
    print(a)#子进程是从fork（）下一句开始执行，但是会继承父进程的全部内存空间，有赋值语句的话，子进程也会有赋值这部分的内存空间

    a=1000#只有子进程执行这个模块，父进程不执行，不影响父进程中a的值
#父进程执行部分
else:
    sleep(1)
    print(a)#打印：1
    print("the process is new")

print(a)#子进程值为1000，父进程值为1（父进程fork之前开辟的空间子进程同样拥有，父子进程对各自空间的操作不会相互影响。）

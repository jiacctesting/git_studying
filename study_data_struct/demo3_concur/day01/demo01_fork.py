"""
windows上运行失败，因为windows上没有fork
正常流程：
运行这个程序分配一个pid，
然后执行os.fork（）会再分配一个pid，例如子进程pid是1234
此时有两个进程，由于调用fork，父进程的pid会被赋值为子进程数1234，而子进程pid赋值会为0，这都是因为fork方法，实际是两遍代码分别执行
子进程是从fork（）下一句开始执行，但是会继承父进程的全部内存空间，有赋值语句的话，子进程也会有赋值这部分的内存空间
所以最终会有四句打印结果
the process is new
the process is old
the process is new
the process is new
打印顺序每次可能会变化，因为两个进程互不影响
"""
import os

#创建子进程
pid = os.fork()

if pid<0:
    print("the process failed")

#子进程执行部分
elif pid==0:
    print("the process is new")

#父进程执行部分
else:
    print("the process is new")

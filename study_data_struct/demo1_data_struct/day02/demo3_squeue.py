"""
队列的顺序存储：
    思路：
        1：依然使用列表来表示
        2：封装列表的功能，对外提供判断是否为空、入队、出队操作
        3：确定队头队尾
"""

class SQueueError(Exception):
    pass

class SQueue:
    def __init__(self):
        self._eles=[]

    def is_empty(self):
        return self._eles==[]

    def enqueue(self,val):
        self._eles.append(val)

    def dequeue(self):
        if not self._eles:
            raise SQueueError("squeue is empty")
        return self._eles.pop(0)




#面试题，如何将现有的队列0-9改成9-0
if __name__=="__main__":
    sq=SQueue()
    for i in range(10):
        sq.enqueue(i)

    from demo1_sstack import *
    st=SStack()
    #循环出队入栈
    while not sq.is_empty():
        st.push(sq.dequeue())
    #循环出栈入队
    while not st.is_empty():
        sq.enqueue(st.pop())

    while not sq.is_empty():
        print(sq.dequeue())


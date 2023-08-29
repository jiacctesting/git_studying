"""
链式队列：
    思路：
        1：基于链表构建队列模型
        2：链表的开端作队头，结尾位置做队尾
        3：段都定义队尾标记，避免每次插入数据遍历
        4：队尾和队头重叠认为队列为空

队头用front，队尾用rear，每次插入节点代表rear移动，每次出队则移动front，之前是head指向None，
现在改成front，front指向哪个元素就代表哪个元素已经出队（类似之前指向哪个哪个就是栈顶）

self.rear.next=Node(val)
self.rear=self.rear.next
这种代码应该注意是否要创建一个变量代替Node(val)，也要注意self.rear是写等于Node()还是写 self.rear=self.rear.next
"""
class LQueueError(Exception):
    pass

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class LQueue:
    def __init__(self):
        self.front=self.rear=Node(None)

    def is_empty(self):
        return self.front==self.rear

    #入队 尾部动，头部不动
    def enqueue(self,val):
        self.rear.next=Node(val)
        self.rear=self.rear.next

    #出队 头动尾部不动
    def dequeue(self):
        if self.is_empty():
            raise LQueueError("queue is empty")
        self.front=self.front.next  #front指向哪个元素就代表哪个元素已经出队（类似之前指向哪个哪个就是栈顶）
        return self.front.val

if __name__=="__main__":
    lq=LQueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    lq.enqueue(40)
    print(lq.dequeue())

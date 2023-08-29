"""
单链表
"""
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


class Linklist:
    def __init__(self,):
        self.head=Node(None)

    #通过list_为链表增加一组节点
    def init_list(self,list_):
        """
        链表初始化
        """
        p=self.head
        for item in list_:
            p.next=Node(item)
            p=p.next
            # p=Node(item)  #直接写p=Node(item)相当于没有把链表连接起来,相当于创建了一个新的链表？？？


    def show(self):
        """
        遍历链表
        """
        p=self.head.next
        while p is not None:
            print(p.val)
            p=p.next

    def is_empty(self):
        """
        判断链表是否为空
        :return: True表示链表为空，False表示链表不为空
        """
        p=self.head
        if p.next is None:
            return True
        else:
            return False

    def clear(self):
        self.head.next=None

    def append(self,val):
        """在尾部增加一个值"""
        p=self.head
        while p.next is not None:
            p=p.next
        p.next=Node(val)

    def head_insert(self,val):
        """在头部增加一个值"""
        node=Node(val)
        node.next=self.head.next
        self.head.next=node

    def insert(self,index,val):
        """在索引值等于index的位置插入val"""
        p=self.head
        for item in range(index):
            """超出链表长度，结束循环，把值加到列表的最后"""
            if p.next is None:
                break
            p=p.next
        node = Node(val)
        node.next = p.next
        p.next = node

    def remove(self,x):
        """删除某个值"""
        p = self.head
        """只有不满足while中的条件时才会结束循环"""
        while p.next and p.next.val!=x:
            p=p.next
        """while判断包含两个条件时，在后边需要以此判断是符合哪个条件导致循环结束的"""
        if p.next is None:
            raise ValueError("x is not in linklist")
        else:
            p.next=p.next.next

        # while p.next is not None:
        #     if p.next.val==x:
        #         p.next=p.next.next
        #     p=p.next
    def get_index(self,index):
        """获取某个index位置上的值"""
        p=self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("index out of range")
            p=p.next
        return p.val

    # def merge(self,list_new):
    #     for item in list_new:
    #         self.head.val = 0
    #         p = self.head
    #         while p.next is not None:
    #             if p.val<item and p.next.val > item:
    #                 node = Node(item)
    #                 node.next = p.next
    #                 p.next = node
    #             else:
    #                 p=p.next





if __name__=="__main__":
    l1=Linklist()
    l2=Linklist()
    l1.init_list([1,2,3,7,10,14,18,19])
    l2.init_list([4,8,11,15,20])
    def merge(l1,l2):
        p=l1.head
        q=l2.head.next
        while p.next is not None:
            if p.next.val<q.val:
                p=p.next
            else:
                tmp=p.next
                p.next=q
                q=tmp
                p=p.next
        p.next=q
    merge(l1,l2)
    l1.show()





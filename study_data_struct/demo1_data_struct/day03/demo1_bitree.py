from demo1_data_struct.day02.demo3_squeue import *

#了解树结构的取值流程即可
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Bitree:
    def __init__(self,root):
        self.root=root

    #先序遍历
    def preOrder(self,node):
        if node is None:
            return
        print(node.val,end=" ")
        self.preOrder(node.left)
        self.preOrder(node.right)

    #中序遍历
    def inOrder(self,node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.val,end=" ")
        self.inOrder(node.right)


    # 后序遍历
    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.val,end=" ")

    #层次遍历
    def levelOrder(self,node):
        sq=SQueue()
        sq.enqueue(node)
        while not sq.is_empty():
            node=sq.dequeue()
            print(node.val)
            if node.left:
                sq.enqueue(node.left)
            if node.right :
                sq.enqueue(node.right)



if __name__=="__main__":
    b=Node("B")
    f=Node("F")
    g=Node("G")
    d=Node("D",f,g)
    h=Node("I")
    i=Node("H")
    e=Node("E",i,h)
    c=Node("C",d,e)
    a=Node("A",b,c)


    bt=Bitree(a)
    bt.preOrder(a)
    print("=======")
    bt.inOrder(a)
    print("=======")
    bt.postOrder(bt.root)
    print("=======")
    bt.postOrder(a)
    print("=======")

    bt.levelOrder(a)

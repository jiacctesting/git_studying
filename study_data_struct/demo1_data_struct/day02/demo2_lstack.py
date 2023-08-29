"""
栈的链式结构：
    思路：用self.top标记栈顶，不管到底有多少元素，top指向的就是栈顶，移动top就可以
栈的应用：在浏览器打开多个页面后，点击返回按钮，依次返回前一页，最后显示的页面是最开始打开的页面

"""
class LStackError(Exception):
    pass
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class LStack:
    def __init__(self):
        #标记栈顶节点
        self._top=None

    def is_empty(self):
        return self._top is None

    def push(self,val):
        # node=Node(val)
        # node.next=self._top
        # self._top=Node
        #三行代码可以优化成一行,node.next=self._top可以直接写到Node()创建对象的时候
        self._top=Node(val,self._top)
    def pop(self):
        """top指向谁谁就是栈顶，所以不用管移动top后的空置元素"""
        if self._top is None:
            raise LStackError("LStack is empty")
        value=self._top.val
        self._top=self._top.next
        return value

    def show_top(self):
        if self._top is None:
            raise LStackError("LStack is empty")
        return self._top.val

if __name__=="__main__":
    ls=LStack()
    ls.push(10)
    ls.push(20)
    ls.push(30)
    print(ls.show_top())
    print(ls.pop())
    print(ls.show_top())

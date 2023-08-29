"""
栈的顺序存储：
    思路：利用列表来模拟线性结构
        因为列表操作太灵活，与列表并不完全一致通过对列表功能的封装，实现栈的功能
栈的应用：在浏览器打开多个页面后，点击返回按钮，依次返回前一页，最后显示的页面是最开始打开的页面
"""


class SStackError(Exception):
    pass


class SStack:
    def __init__(self):
        self._ele = []

    def is_empty(self):
        # 通过判断self.ele是否与空列表相等来判断列表是否为空，结果是true/false
        return self._ele == []

    def push(self, val):
        self._ele.append(val)

    def pop(self):
        if self.is_empty():
            raise SStackError("sstrack is empty")
        return self._ele.pop()

    def top(self):
        if self.is_empty():
            raise SStackError("sstrack is empty")
        return self._ele[-1]


"""应用：逆波兰表达式"""
if __name__=="__main__":
    st = SStack()
    while True:
        exp = input()
        tmp = exp.split(" ")
        for i in tmp:
            if i not in ["+", "-", "*", "/", "p"]:
                st.push(float(i))
            elif i == "+":
                y = st.pop()
                x = st.pop()
                st.push(x + y)
            elif i == "-":
                y = st.pop()
                x = st.pop()
                st.push(x - y)
            elif i == "*":
                y = st.pop()
                x = st.pop()
                st.push(x * y)
            elif i == "/":
                y = st.pop()
                x = st.pop()
                st.push(x / y)
            elif i == "p":
                print(st.top())

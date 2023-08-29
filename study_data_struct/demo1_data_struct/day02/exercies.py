"""
找出[] {} ()判断是否完整
"""
content="This tool helps you learn {Python}, (JavaScript, C, C++), " \
        "and [Java programming] by visualizing code execution. " \
        "You can use it (to debug [your homework) assignments and as a supplement to online coding tutorials."
list_result=[]
for item in content:
    if item in ["{","}","(",")","[","]"]:
        list_result.append(item)
print(list_result)
print("{"+"}")
print(type("{"+"}"))
from demo1_sstack import  *
st=SStack()
for item in list_result:
    if item in ["{","(","["]:
        st.push(item)
    if item in ["}",")","]"]:
        merge=st.pop()+item
        if merge in ["{}","[]","()"]:
            continue
        else:
            print("括号不正确，不正确的是"+st.top() )
            break
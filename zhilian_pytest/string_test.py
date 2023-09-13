#请写一个 Python 函数，接受一个字符串，返回该字符串中每个字符出现的次数。
import copy


def count_times(s):
    dic={}
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    print(dic)

a=[1,2,[3,4]]
b=a.copy()
a[2][1]=0
print("a:",a)
print("b:",b)

c=copy.deepcopy(a)
a[2][1]=1

print("c:",c)
if __name__ == '__main__':
    count_times("yuwesss")




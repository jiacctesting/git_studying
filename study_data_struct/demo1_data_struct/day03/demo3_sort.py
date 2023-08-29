
#排序练习
def func(l):
    for i in range(len(l)-1):
        for j in range(i,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
#冒泡排序
def bubble(l):
    #外层表示循环多少轮
    for i in range(len(l)-1):
        #内层表示每轮两两比较的次数
        for j in range(len(l)-1-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
# l=[1,6,3,7,8,4,5,0]
# bubble(l)
# print(l)

#快排  掌握流程即可
def sort(list_,low,high):
    x=list_[low]
    while low<high:
        while list_[high]>=x and low<high:
            high-=1
        else:
            list_[low]=list_[high]
        while list_[low]<x and low<high:
            low+=1
        else:
            list_[high]=list_[low]
    else:
        list_[high]=x
    return high

def quick(list_,low,high):
    if low<high:
        key=sort(list_,low,high)
        sort(list_,low,key)
        sort(list_,key+1,high)

# l01=[4,9,3,1,2,5,8,4]
# quick(l01,0,7)
# print(l01)

#选择排序
def select(list_):
    #每轮选出一个最小值，需要len(list_)-1轮
    for i in range(len(list_)-1):
        min=i#假设list[i]是最小值
        for j in range(i+1,len(list_)):
           if  list_[min]>list_[j]:
               min=j#擂主换人
        #进行交换，将最小值换到应该在的位置
        if min!=i:
            list_[min],list_[i]=list_[i],list_[min]

#插入排序
def insert(list_):
    for i in range(1,len(list_)):
        x=list_[i]
        j=i-1
        while j>=0 and list_[j]>x:
            list_[j+1]=list_[j]
            j-=1
        else:
            list_[j+1]=x





l01=[4,9,3,1,2,5,8,4]
insert(l01)
print(l01)

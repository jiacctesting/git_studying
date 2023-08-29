"""
二分查找
"""

#自己写的不精简，思路略微有点乱
# def is_in(list_,key,start,end):
#     if key in list_[start:end]:
#         return True
#     return False
# def search(list_,key):
#     i=len(list_)-1
#     while True:
#         while is_in(list_,key,0,i//2) and (i-((i//2)+1))>1:
#             i//=2
#         while is_in(list_,key,(i//2)+1,i) and (i-((i//2)+1))>1:
#             i=((i//2)+1+i)//2
#         return i


#二分法查找
def search(list_,key):
    low,high=0,len(list_)-1
    while low<=high:
        mid = (low + high) // 2
        if key<list_[mid]:
            high=mid-1
        elif key>list_[mid]:
            low=mid+1
        else:
            return mid

l=[1,2,3,4,5,6]
# print(l.index(4))
# print(len(l))
# print((len(l))//2)
print("search index",search(l,60))
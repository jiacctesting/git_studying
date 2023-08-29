def bubble(l):
    for i in range(len(l)-1):
        for j in range(i,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]

l=[1,6,3,7,8,4,5,0]
bubble(l)
print(l)
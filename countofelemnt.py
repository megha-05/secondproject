n=int(input("enter no of elements in array"))
list1=[]
flag=0
for i in range(0,n):
    n=int(input())
    list1.append(n)
print(list1)
count=0
for i in range(0,n):
    c=list1.count(list1[i])
    if(c>n//2):
        num=list1[i]
        flag=0
        break
    else:
        flag=1
def number(list1,num):
    while num in list1:
        list1.remove(num)
    return list1
if(flag==1):
    print("none")
else:
    list1=number(list1,num)
    print(list1)
    
    
        
    
    

a=int(input("enter the no of elemts in list"))
i=0
j=0
avg=0
list1=[]
for i in range(0,a):
    num=int(input())
    list1.append(num)
print(list1)
while(list1[i]!=-1):
    for i in range(0,a):
        for j in range(0,a):
            if(list1[i]<list1[j]):
                temp=list1[i]
                list1[i]=list1[j]
                list1[i]=temp
print(list1)
newsum=sum(list1)
avg=newsum/a
print(avg)
small=0
large=0
diff=0
for i in range(0,a):
    if(list1[i]>large):
        large=list1[i]
print(large)
for i in range(0,a):
    if(small<list[i]):
        small=list1[i]
print(small)
diff=large-small
print(diff)

        
        
 
                
                
    

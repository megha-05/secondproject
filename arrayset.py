n=input("enter a number")
list1=[]
list2=[]
set1=set()
set2=set()
list1=n.split(" ")
array=list()
n1=input("enter arrya elements")
array=n1.split(" ")
num=input("enter number of set a")
num3=input("enter no of elemnts of set b")
set1=num.split(" ")
set2=num3.split(" ")
length=len(array)
happiness=0
for i in range(0,length):
        n1=array[i]
        if n1 in set1:
            happiness+=1
        elif n1 in set2:
            happiness-=1
        else:
            happiness=0
print(happiness)

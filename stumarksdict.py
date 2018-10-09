dict1={}
dict2={}

for i in range(0,4):
    name=(input("enter name"))
    m1=int(input("enter the marks"))
    m2=int(input("enter the marks"))
    m3=int(input("enter the marks"))
    m4=int(input("enter the marks"))
    total=m1+m2+m3+m4
    dict2[name]=total
print(dict2)    

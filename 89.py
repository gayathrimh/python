n1=123456
len1=len(str(n1))
n2=n1
list1=[]
for i in range(0,5,1):
    list1.append(str(n2%10))
    n2=n2//10
s1="".join(list1)
print(s1)

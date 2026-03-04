def factorial1(n):
    fact1=n
    for i in range(n,2,-1):
        fact1=fact1*(i-1)
    return fact1
def factorial2(list1):
    list2=[]
    for i in range(0,3,1):
        temp=factorial1(list1[i])
        list2.append(temp)
    return list2
n=5
list1=[5,6,7,8]
result=factorial1(n)
print("factorial of",n,"is",result)
result=factorial2(list1)
print("factorial of",list1,"is",result)

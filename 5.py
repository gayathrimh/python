def calc(n1,n2):
    sum1=n1+n2
    diff1=n1-n2
    prd1=n1*n2
    div1=n1/n2
    div2=n1//n2
    rem1=n1%n2
    exp1=n1**n2
    list1=[]
    list1.append(sum1)
    list1.append(diff1)
    list1.append(prd1)
    list1.append(div1)
    list1.append(div2)
    list1.append(rem1)
    list1.append(exp1)
    return list1
start=input("enter first no")
end=input("enter second no")
n1=int(start)
n2=int(end)
result=calc(n1,n2)
print(result)

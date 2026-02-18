def calc2(num1,num2):
    sum1=num1+num2
    dif1=num1-num2
    prd1=num1*num2
    div1=num1/num2
    div2=num1//num2
    rem1=num1%num2
    exp1=num1**num2
    
    list1=[]
    list1.append(sum1)
    list1.append(dif1)
    list1.append(prd1)
    list1.append(div1)
    list1.append(div2)
    list1.append(rem1)
    list1.append(exp1)
    return list1
    print(sum1,dif1,prd1,div1,div2,rem1,exp1)
result=calc2(8,4)
print(result)


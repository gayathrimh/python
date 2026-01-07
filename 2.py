def calc(n1,n2):
    sum1=n1+n2
    diff1=n1-n2
    prd1=n1*n2
    div1=n1/n2
    div2=n1//n2
    rem1=n1%n2
    list=[]
    list.append(sum1)
    list.append(diff1)
    list.append(prd1)
    list.append(div1)
    list.append(div2)
    list.append(rem1)
    return list

    print(sum1,diff1,prd1,div1,div2,rem1)
calc(10,2)
calc(2,10)
calc(8,4)


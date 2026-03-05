def factors(n):
    list2=[1]
    for i in range(2,n+1,1):
        if n%i==0:
            list2.append(i)
    return list2
print(factors(12))

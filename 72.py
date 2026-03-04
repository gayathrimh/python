def factorial1(n):
    fact1=n
    for i in range(n,2,-1):
        fact1=fact1*(i-1)
    return fact1
n=5
result=factorial1(n)
print("factorial of",n,"is",result)

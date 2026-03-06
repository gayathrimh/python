list1=[0,1]
num1,num2=0,1
sum1=num1+num2

for i in range(0,10,1):
    num1=num2
    num2=sum1
    sum1=num1+num2
    list1.append(sum1)
print(list1)

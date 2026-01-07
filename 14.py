<<<<<<< HEAD
#2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,61,67,71,73,77,79,81,83,87,89,91,97

list1=[2,3]
print(list1)
num1=4
isPrime=True
if num1%2==0:
  isPrime=False
if num1%3==0:
  isPrime=False
if isPrime==True:
    list1.append(num1)
print(list1)

num1=5
isPrime=True
if num1%2==0:
    isPrime=False
if num1%3==0:
    isPrime==False
if isPrime==True:
    list1.append(num1)
    print(list1)

num1=6
isPrime=True
if num1%2==0:
    isPrime=False
if num1%3==0:
    isPrime=False
if num1%4==0:
    isPrime=False
if num1%5==0:
    isPrime=False
if isPrime==True:
    list1.append(num1)
    print(list1)

num1=7
isPrime=True
if num1%2==0:
    isPrime=False
if num1%3==0:
    isPrime=False
if num1%4==0:
    isPrime=False
if num1%5==0:
    isPrime=False
if num1%6==0:
    isPrime=False
if isPrime==True:
    list1.append(num1)
    print(list1)
=======
f1=open("in2.txt","r")
f2=open("out1.txt","w")
s1=f1.readline().strip()
list1=s1.split(",")
n1=int(list1[0])
n2=int(list1[1])
for j in range(n1,n2+1,1):
    
    for i in range(1,11,1):
        print(j,i,j*i)
        f2.write(str(j)+"*"+str(i)+"="+str(j*i))
        f2.write("\n")
    print()
    f2.write("\n")
f2.close()
>>>>>>> 2662dd6074379fe70661297c0b2e2e35399080c9

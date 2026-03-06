#Reverse a number

n=1234
list1=[]
temp1=n%10   #4
temp2=n//10  #123
list1.append(str(temp1))

n=temp2
temp1=n%10  #3
temp2=n//10 #12
list1.append(str(temp1))

n=temp2
temp1=n%10  #2
temp2=n//10 #1
list1.append(str(temp1))

n=temp2
temp1=n%10  #1
temp2=n//10
list1.append(str(temp1))
print(list1)
s1="".join(list1)   #Join list into string
print(s1)

def square1(n):
    return n*n
def square2(list1):
    list2=[]
    len1=len(list1)
    for i in range(0,len1,1):
        temp=square1(list1[i])
        list2.append(temp)
    return list2
n=5
list1=[5,6,7,8,9,10,11,12,13,14]
result=square1(n)
print("square of",n,"are",result)
result=square2(list1)
print("square of",list1,"are",result)

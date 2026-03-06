list1=[1,1]
for i in range(0,10,1):
    pos=i
    item1=list1[pos]
    item2=list1[pos+1]
    item3=item1+item2
    list1.append(item3)
print(list1)

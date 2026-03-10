f1=open("marks.txt","r")
names=[]
sub1=[]
sub2=[]
sub3=[]
sub4=[]
sub5=[]
subjects=[]
total=[]
toppersSub1=[]
toppersSub2=[]
toppersSub3=[]
toppersSub4=[]
toppersSub5=[]
goldmedalist=[]

for i in range(0,26,1):
    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
    
    list2=list1[3].split(":")
    sub1.append(int(list2[1]))
    subjects.append(list2[0])

    list2=list1[4].split(":")
    sub2.append(int(list2[1]))
    subjects.append(list2[0])

    list2=list1[5].split(":")
    sub3.append(int(list2[1]))
    subjects.append(list2[0])

    list2=list1[6].split(":")
    sub4.append(int(list2[1]))
    subjects.append(list2[0])

    list2=list1[7].split(":")
    sub5.append(int(list2[1]))
    subjects.append(list2[0])

    total.append(sub1[i]+sub2[i]+sub3[i]+sub4[i]+sub5[i])
    

maxSub1=max(sub1)
maxSub2=max(sub2)
maxSub3=max(sub3)
maxSub4=max(sub4)
maxSub5=max(sub5)

#print(names)
#print(sub1)
#print(sub2)
#print(sub3)

for i in range(0,26,1):
    if sub1[i]==maxSub1:
        toppersSub1.append(names[i])
    if sub2[i]==maxSub2:
        toppersSub2.append(names[i])
    if sub3[i]==maxSub3:
        toppersSub3.append(names[i])
    if sub4[i]==maxSub4:
        toppersSub4.append(names[i])
    if sub5[i]==maxSub5:
        toppersSub5.append(names[i])
print(toppersSub1,"are toppers in ",subjects[0]," with marks ",maxSub1)
print(toppersSub2,"are toppers in ",subjects[1],"with marks ",maxSub2)
print(toppersSub3,"are toppers in",subjects[2],"with marks",maxSub3)
print(toppersSub4,"is topper in",subjects[3],"with marks",maxSub4)
print(toppersSub5,"is topper in",subjects[4],"with marks",maxSub5)

print(total)

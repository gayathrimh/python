countries=[]
capitals=[]
marks=[]
f1=open("gk1.txt","r")
for i in range(0,10,1):
    s1=f1.readline().strip()
    list1=s1.split(",")
    countries.append(list1[0])
    capitals.append(list1[1])
print(countries)
print(capitals)
for i in range(0,3,1):
    r1=input("what is capital of"+countries[i])
    if r1==capitals[i]:
        marks.append(10)
    else:
        marks.append(0)
print(marks)
print("you have scored",sum(marks),"marks")
for i in range(0,3,1):
    if marks[i]==0:
        print("correct answer is",i+1,capitals[i])

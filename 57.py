f1=open("in2.txt","r")
s1=f1.readline().strip()
list1=s1.split(",")
n1=int(list1[0])
n2=int(list1[1])
f1.close()

for j in range(n1,n2+1,1):
    filename=str(j)+".txt"
    f2=open(filename,"w")
    for i in range(1,11,1):
        print(j,i,j*i)
        f2.write(str(j)+"*"+str(i)+"="+str(j*i))
        f2.write("\n")
    print()
    f2.write("\n")
f2.close()  

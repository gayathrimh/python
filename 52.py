start=int(input("enter first no"))
end=int(input("enter second no"))

for j in range(start,end+1,1):
    for i in range(1,11,1):
        print(j,i,j*i)
    print()
    

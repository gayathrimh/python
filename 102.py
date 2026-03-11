s1="Funwith"
len1=len(s1)
for i in range(1,len1+1,1):
    print(" "*(len1-i)+s1[0:i])
for i in range(1,len1,1):
    print(" "*i+s1[0:len1-i])

def diamondright(s1):
    len1=len(s1)
    for i in range(1,len1+1,1):
        print(s1[0:i])
    for i in range(0,len1-1,1):
        print(s1[0:len1-1-i])
        
diamondright("gayathri")
diamondright("dhyan")

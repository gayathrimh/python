def diamondleft(s1):
    len1=len(s1)
    spaces=" "
    for i in range(1,len1+1,1):
        print(spaces*(len1-i)+s1[0:i])
    for i in range(1,len1,1):
        print(spaces*i+s1[0:len1-i])

diamondleft("Udupiparyaya")


def getPassword1(size1):
    import random as rd
    pwd1=""
    s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s2="abcdefghijklmnopqrstuvwxyz"
    d1="0123456789"
    upper1=list(s1)
    lower1=list(s2)
    digits1=list(d1)
    full=upper1+lower1+digits1
    rd1=rd.randint(0,25)
    pwd1=pwd1+s1[rd1]
    rd1=rd.randint(0,25)
    pwd1=pwd1+s2[rd1]
    rd1=rd.randint(0,9)
    pwd1=pwd1+d1[rd1]
    for i in range(0,size1-3,1):
        rd1=rd.randint(0,61)
        pwd1=pwd1+full[rd1]
    list1=list(pwd1)
    rd.shuffle(list1)
    pwd2="".join(list1)
    print(pwd2)
getPassword1(20)

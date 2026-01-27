def passGen2(size1,qty1):
    def passGen1(size1):
        import random as rd
        s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s2="abcdefghijklmnopqrstuvwxyz"
        d1="0123456789"
        list1=list(s1)
        list2=list(s2)
        list3=list(d1)
        list4=list1+list2+list3
        pwd1=""
        pwd1=pwd1+rd.choice(list1)
        pwd1=pwd1+rd.choice(list2)
        pwd1=pwd1+rd.choice(list3)
        for i in range(0,size1-3,1):
            pwd1=pwd1+rd.choice(list4)
        temp=list(pwd1)
        rd.shuffle(temp)
        pwd2="".join(temp)
        print(pwd2)
    for i in range(0,qty1,1):
        passGen1(size1)


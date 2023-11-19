a,b=map(int,input().split())
d=28
d1=29
d2=30
d3=31
if a>12 or a<1:
    print("INVALID")
else:
    if  a==2:
        if b%4==0:
            print(d1)
        else:
            print(d)
    else:
        if a== 2:
            print(d)
        elif (a==1 or a==3) or (a==5 or a==7) or (a==8 or a==10) or a==12:
            print(d3)
        elif (a==4 or a==6) or (a==9 or a==11):
            print(d2)
from decimal import Decimal

def Convert(s):
    if s==1:
        return "1"
    elif s==0:
        return "0"
    else :
        return Convert(s//2)+str(s%2)
test=int(input())
while test>0:
    test-=1
    s=Decimal(input())
    n=Convert(s)
    print(n)
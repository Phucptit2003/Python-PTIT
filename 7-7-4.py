from decimal import Decimal

def cnt(n):
    num=Decimal(n)
    string_num=str(num)
    c=len(string_num)
    if string_num[0]=='-':
        c-=1
    return c
        
string=input()
n=cnt(string)
print(n)
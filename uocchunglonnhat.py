def check(a,b):
    if b==0:
        return a
    return check(b,a%b)

a,b=map(int,input().split())

if a<0:
    a=-1*a
if b<0:
    b=-1*b
print(check(a,b))
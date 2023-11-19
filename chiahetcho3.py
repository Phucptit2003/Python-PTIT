def check(a,b):
    arr=[]
    for i in range (a,b+1,-1):
        if i%3==0:
            arr.append(i)
    return arr


a,b=map(int,input().split())
if a<0:
    a=-1*a
if b<0:
    b=-1*b
print(check(a,b))
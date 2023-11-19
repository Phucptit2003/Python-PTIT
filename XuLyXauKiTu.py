s=input()
s1=input()
a=s.split()
b=s1.split()
tmp=[]
res=[]
for i in a:
    if i.lower() not in tmp:
        tmp.append(i.lower())
for i in b:
    if i.lower() not in tmp:
        tmp.append(i.lower())
    elif i.lower() in tmp and i.lower() not in res:
        res.append(i.lower())
tmp.sort()
res.sort()
print(*tmp)
print(*res)
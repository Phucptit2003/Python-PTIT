def check(s):
    if s==s[::-1]:
        return True
    else:
        return False
n,m=map(int,input().split())
maxx=0
tmp=[]
for i in range(n):
   tmp.append([int(x) for x in input().split()])
for i in range(n):
    for j in range(m):
        if check(str(tmp[i][j])) and len(str(tmp[i][j]))>=2:
            if tmp[i][j]>maxx:
                maxx=tmp[i][j]
if maxx==0:
    print("NOT FOUND")
else:
    print(maxx)
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==maxx:
                s="Vi tri ["+str(i)+"]["+str(j)+']'
                print(s)
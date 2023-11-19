def check(s,q,r):
    gia=0
    if r=="IN":
        if s=="Xe_con":
            if int(q)==5:
                gia=10000
            else:
                gia=15000
        elif s=="Xe_tai":
            gia= 20000
        else:
            if int(q)==29:
                gia=50000
            else:
                gia= 70000
    return gia
        

n=int(input())
res=[]
for _ in range(n):
    res.append(input().split())
day=[]
for i in res:
    if i[4] not in day:
        day.append(i[4])
for i in day:
    sum=0
    for j in res:
        if j[4]==i:
            sum+=check(j[1],j[2],j[3])
    print(f"{i}: {sum}")

       
    
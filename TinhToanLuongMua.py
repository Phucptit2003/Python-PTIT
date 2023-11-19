n=int(input())
arr=[]
t=1
for _ in range(n):
    name=input()
    begin=str(input())
    end=str(input())
    luongmua=int(input())
    time=(int(end[0])*10+int(end[1]))*60+(int(end[3])*10+int(end[4]))-(int(begin[0])*10+int(begin[1]))*60+(int(begin[3])*10+int(begin[4]))
    check=False
    for i in arr:
        if name in i:
            check=True
            break
    if check==False:
        s="T{:02d}".format(t)
        t+=1
        arr.append((s,name,time,luongmua))
    else:
        for i in arr:
            if name==i[0]:
                i[2]+=time
                i[3]+=luongmua
for i in arr:
    print(i[0]+" "+i[1])

                

test=int(input())
tmp=[]
for _ in range(test):
    name=input()
    a=name.split()
    dvi=input()
    b=dvi.split()
    time=input()
    id=""
    for s in b:
        id+=s[0].upper()
    for s in a:
        id+=s[0].upper()
    t=(int(time[0])-6)+(int(time[2])*10+int(time[3]))/60
    v=round(120/t)
    tmp.append((id,name,dvi,v,time))
tmp.sort(key=lambda x : (x[4]))
for s in tmp:   
    print(f"{s[0]} {s[1]} {s[2]} {s[3]} Km/h")
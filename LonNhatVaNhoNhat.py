def Check(x):
    check=False
    s=""
    for i in x:
        if i!='0':
            check=True
        if check==True:
            s+=i
    return s

while True:   
    n=int(input())
    if n==0:
        break
    else:
        tmp=[]
        for _ in range(n):
            x=int(input())
            tmp.append(x)
        tmp.sort()
        if tmp[0]==tmp[len(tmp)-1]:
            print("BANG NHAU")
        else:
            print(f"{tmp[0]} {tmp[len(tmp)-1]}")
def check2(s):
    for i in s:
        if i<='a' or i>='z':
            return False
    return True

def Tach(s):
    res=""
    for i in s:
        if (i>='a' and i<='z') or (i>='0' and i<='9'):
            if i>='a' and i<='z':
                res+=i
        else:
            res+=" "
    return res

n=int(input())
tmp=[]
for _ in range(n):
    s=input()
    arr=s.split()
    for i in arr:
        if check2(i.lower())==False:
            a=Tach(i.lower()).split()
            for j in a:
                tmp.append(j)
        else:
            tmp.append(i.lower())
res={}
for i in tmp:
    if i in res:
        res[i]+=1
    else:
        res[i]=1
res_sort=sorted(res.items(), key=lambda x: (-x[1],x[0]))
    
for word,cnt in res_sort:
    print(f"{word} {cnt}")
           
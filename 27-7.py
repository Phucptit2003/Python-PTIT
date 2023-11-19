def check(b,c,h):
    cnt=2
    b-=2
    c1=False
    c2=False
    if b>0:
        while c>0:
            c-=1
            b-=1
            cnt+=2
            if b==0:
                cnt+=1
                c1=True
                break
        if c1==False:
            while h>0:   
                if h==1 and b>0:
                    cnt+=1
                    break
                elif b==0 and h>0:
                    cnt+=1
                    break
                h-=1
                b-=1
                cnt+=2
    else:
        cnt+=1
    return cnt

test=int(input())
for _ in range(test):
    b,c,h=map(int,input().split())
    result=check(b,c,h)
    print(result)
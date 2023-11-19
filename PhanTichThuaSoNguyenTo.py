test=int(input())
for _ in range(test):
    n=int(input())
    i=2
    tmp=""
    tmp+="1"
    while(n>1):
        if(n%i==0):
            cnt=0
            tmp+=" * "+str(i)+"^"
            while n%i==0:
                cnt+=1
                n/=i
            tmp+=str(cnt)
        else:
            i+=1
    print(tmp)
            
            
            
    
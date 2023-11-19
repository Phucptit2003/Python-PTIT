test=int(input())
for _ in range(test):
    n,m,k=map(int,input().split())
    x=[int(i) for i in input().split()]
    y=[int(i) for i in input().split()]
    z=[int(i) for i in input().split()]
    i=j=t=0
    check=0
    while i<n and j<m and t<k:
        if x[i]==y[j]==z[t]:
            print(x[i],end=" ")
            check=1
            i+=1
            j+=1
            t+=1
        elif x[i]<y[j]:
            i+=1
        elif y[j]<z[t]:
            j+=1
        else:
            t+=1
    if check==0:
        print("NO")
    else:
        print()
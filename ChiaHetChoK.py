a,k,n=map(int,input().split())
minn=(int(a/k)+1)*k-a
maxx=int(n/k)*k-a
if minn<=maxx:
    for i in range(minn,maxx+1,k):
        print(i,end=" ")
else:
    print("-1")
    
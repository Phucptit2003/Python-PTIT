def Check(n,start,end,mid):
    if n==1:
        print(start,'->',end)
        return
    Check(n-1,start,mid,end)
    print(start,"->",end)
    Check(n-1,mid,end,start)

n=int(input())
Check(n,'A','C','B')
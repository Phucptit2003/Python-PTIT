def Hoanvi(a,check,n):
    i=n-1
    while a[i]>a[i+1] and i>0:
        i-=1
    if i==0:
        check=True
 #       return check
    k=n
    while a[k]<a[i]:
        k-=1
    tmp=a[i]
    a[i]=a[k]
    a[k]=tmp
    l=i+1
    r=n
    while l<r:
        tmp=a[l]
        a[l]=a[r]
        a[r]=tmp
        l+=1
        r-=1
    return a

n,k = map(int,input().split())
arr=[1]*(n)
index=1
for i in range(0,n):
    arr[i]=index
    index+=1
b=arr

check=False
while check==False:
    check1=True
    for i in range(1,n+1):
        if abs(b[i]-arr[i])!=k:
            check1=False
            break
    if check1==True:
        print(arr)
        break
    Hoanvi(arr,check,n)
if check1==False:
    print("-1")

    
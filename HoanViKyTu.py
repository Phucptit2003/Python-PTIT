s=str(input())
n=len(s)
arr=[0]*n
for i in range(n):
    arr[i]=i
while(True):
    for i in range(n):
        print(s[arr[i]],end="")
    print()
    t=n-2
    while arr[t]>arr[t+1]:
        t-=1
    if t<0:
        break
    k=n-1
    while arr[k]<arr[t]:
        k-=1
    tmp=arr[k]
    arr[k]=arr[t]
    arr[t]=tmp
    l=t+1
    r=n-1
    while l<r:
        tmp=arr[l]
        arr[l]=arr[r]
        arr[r]=tmp
        l+=1
        r-=1
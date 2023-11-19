n,k=map(int,input().split())
arr=[int(i) for i in input().split()]
arr.sort()
cnt=1
for i in range(1,n):
    if arr[i]-arr[i-1]>k:
        cnt+=1
print(cnt)
    
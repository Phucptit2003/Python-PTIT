n=int(input())
arr=[]
for _ in range(n):
    arr.append([int(i) for i in input().split()])
if len(arr)==2:
    for x in arr:
        t=x[1]//2
        break
    print(f"{t} {t}")
else:
    a=[0]*(n)
    a[1]=(arr[1][2]+arr[0][1]-arr[0][2])//2
    for i in range(n):
        if i!=1:
            a[i]=arr[1][i]-a[1]
    print(*a)

    
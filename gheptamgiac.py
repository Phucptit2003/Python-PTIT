a,b,c=map(int,input().split())
arr=[]
arr.append(a)
arr.append(b)
arr.append(c)
arr.sort()
time =0
if arr[0]+arr[1]<=arr[2]:
    time=arr[2]-arr[1]-arr[0]+1
print(time)

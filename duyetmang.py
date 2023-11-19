n,k=map(int,input().split())
input_string=input()
arr=input_string.split()
arr=[int(input_string) for input_string in arr]
b=[]
f=
for i in range(n):
    b.append(arr[i]**2)
cnt=0
for j in range(n):
    for i in range(0,j+1):
        if arr[i]+b[j]==k:
            cnt+=1
print(cnt)
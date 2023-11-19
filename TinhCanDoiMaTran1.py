n=int(input())
arr=[]
for i in range(n):
    arr.append([int(i) for i in input().split()])
k=int(input())
up=0
down=0
for i in range(n):
    for j in range(n):
        if i<j:
            up+=arr[i][j]
        elif i>j:
            down+=arr[i][j]
if abs(down - up) >k:
    print("NO")
else:
    print("YES")
print(abs(down-up))

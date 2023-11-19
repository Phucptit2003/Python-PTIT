import math
n=int(input())
col=[0]*(n+1)
row=[0]*(n+1)
for i in range(n):
    matrix=input()
    for j in range(len(matrix)):
        if matrix[j]=='C':
            row[i]+=1
            col[j]+=1
res=0
for i in row:
    if i>=2:
        res+=math.comb(i,2)
for j in col:
    if j>=2:
        res+=math.comb(j,2)
print(res)
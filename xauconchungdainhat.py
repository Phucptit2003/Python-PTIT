a=str(input())
b=str(input())
n1=len(a)
n2=len(b)
f=[ [0]*(n2+1) for _ in range(n1+1)]

for i in range (1,n1+1):
    for j in range(1,n2+1):
        if a[i-1]==b[j-1]:
            f[i][j]=f[i-1][j-1]+1
        else:
            f[i][j]=max(f[i-1][j],f[i][j-1])
            
print(f[n1][n2])
    
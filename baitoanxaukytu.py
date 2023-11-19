m,n= map(int,input().split())
a=str(input())
b=str(input())
tmp=[[0 ]*(n+1) for _ in range(m+1)]
for i in range(m+1):
    for j in range(n+1):
        if i==0 or j==0:
            tmp[i][j]=0
        else:
            if a[i-1]==b[j-1]:
                tmp[i][j]=tmp[i-1][j-1]+1
            else:
                tmp[i][j]=max(tmp[i-1][j],tmp[i][j-1])
            
print(tmp[m][n])
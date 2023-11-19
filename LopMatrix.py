class Matrix:
    def __init__(self,n,m,mt):
        self.n=n
        self.m=m
        self.mt=mt
    
    def __mul__(self):
        res=[]
        for i in range(n):
            res+=[[0]*self.n]
            for j in range(n):
                for k in range(m):
                    res[i][j]+=self.mt[i][k]*self.mt[j][k]
        return Matrix(self.n,self.m,res)
        
    def __str__(self):
        for i in self.mt:
            print(*i)
        return ''

for i in range(int(input())):
    n,m=map(int,input().split())
    mt=[]
    for i in range(n):
        mt.append([int(j) for j in input().split()])
    matrix=Matrix(n,m,mt)
    print(matrix.__mul__())
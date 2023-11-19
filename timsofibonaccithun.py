maxn=pow(10,4)
f=[0]*(maxn+1)
f[0]=1
f[1]=1
for i in range(2,maxn+1):
    f[i]=f[i-1]+f[i-2]

t=int(input())
input_string=input()
arr=input_string.split()
arr=[int(input_string) for input_string in arr]
for i in arr:
    print(f[i])
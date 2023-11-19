n,k=map(int,input().split())
input_string=input()
arr=input_string.split()
arr=[int(input_string) for input_string in arr]
vector=[]
cnt=[0]*(n+2)
for _ in range(k):
    a,b=map(int,input().split())
    pair=[a,b]
    vector.append(pair)
cnt[-1]=0
for i in range(0,n):
    cnt[i]=cnt[i-1]+arr[i]

for pair in vector:
    print(cnt[pair[1]-1]-cnt[pair[0]-2],end=" ")
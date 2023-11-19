n,q=map(int,input().split())
input_string=input()
arr=input_string.split()
arr=[int(input_string) for input_string in arr]
vector=[]
for _ in range(q):
    a,b,c=map(int,input().split())
    pair=[a,b,c]
    vector.append(pair)
cnt=[0]*(n+1)
cnt[-1]=0
for i in range(0,n):
    cnt[i]=cnt[i-1]+arr[i]
for pair in vector:
    if pair[0]==1:
        cnt[pair[1]-1]+=pair[2]
    else:
        if 
        print(cnt[pair[2]-1]-cnt[pair[1]-2],end=" ")
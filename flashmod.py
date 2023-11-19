c1,n=map(int,input().split())
vector=[]
for _ in range(n):
    a,b=map(int,input().split())
    pair=[a,b]
    vector.append(pair)
dem=1
for pair in vector:
    if int(pair[1])==c1:
        dem+=1
        c1=int(pair[0])
print(c1,end=" ")
print(dem)

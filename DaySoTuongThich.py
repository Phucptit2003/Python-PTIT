def check(tmp,arr):
    for i in range(len(tmp)-1):
        if arr[i]//tmp[i]!=arr[i+1]//tmp[i+1]:
            return False
    return True
n=int(input())
arr=[int(i) for i in input().split()]
k=min(arr)
tong=1000000
res=[]
for i in range(1,k+1):
    tmp=[]
    for j in range(n):
        t=arr[j]//(i+1)+1                  
        tmp.append(t)
    if sum(tmp)< tong and check(tmp,arr):
        res=tmp
        tong=sum(tmp)
print(sum(res))
        
    


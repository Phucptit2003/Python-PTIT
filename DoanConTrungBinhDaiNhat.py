n=int(input())
arr=[int(i) for i in input().split()]
length=0
avg=0
for i in range(n-1):
    tong=arr[i]
    k=1
    for j in range(i+1,n):
        tong+=arr[j]
        tb=tong/k
        k+=1
        if tb>avg:
            avg=tb
            length=k
        elif tb==avg:
            length=max(length,k)
    
print(length)
        
    
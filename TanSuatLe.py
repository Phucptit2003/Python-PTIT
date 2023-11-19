test=int(input())
N= 10**6
for _ in range(test):
    n=int(input())
    arr=[int(i) for i in input().split()]
    dd =[0]*(N+1)
    for i in arr:
        dd[i]+=1
    for i in arr:
        if dd[i]%2==1:
            print(i)
            break
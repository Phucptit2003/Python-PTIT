n,x,y=map(int,input().split())
input_string=input()
arr=input_string.split()
arr=[int(input_string) for input_string in arr]
if x>y:
    print(n)
else:
    dem=0
    for i in arr:
        if i<=x:
            dem+=1
    if dem//2<dem/2:
        cnt=dem//2+1
    else:
        cnt=dem//2
    print(cnt)
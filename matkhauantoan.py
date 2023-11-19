n=int(input())
for _ in range(n):
    input_string=str(input())
    dem=0
    check=False
    check1=False
    check2=False
    for i in input_string:
        if i>='0' and i<='9':
            check=True
        elif i>='A' and i<='Z':
            check1=True
        else:
            check2=True
    if check==True:
        dem+=1
    if check1==True:
        dem+=1
    if check2==True:
        dem+=1
    if dem==1:
        cnt=1
    elif dem==2:
        cnt=2
    else:
        cnt=5
    sum=min(5,max(len(input_string)-5,0))
    print(sum+cnt,end=" ")
        
        
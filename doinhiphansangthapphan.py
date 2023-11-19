
test=int(input())
for _ in range(test):
    string=str(input())
    sum=0
    k=0
    for i in range(len(string)-1,-1,-1):
        if int(string[i])==1:
           sum+=pow(2,k)
        k+=1
    print(sum)         
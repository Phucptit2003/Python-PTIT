dp=[7,6,5,4,3,2]
#8,0,6,9,2,5,3,4,7,1
def check(m):
    if m==7:
        return 8
    elif m==6:
        return 0
    elif m==5:
        return 2
    elif m==4:
        return 4
    elif m==3:
        return 7
    else:
        return 1

n=int(input())
if n>26:
    print("Impossible")
else:
    m=5
    while(n>=dp[m]):
        if n-dp[m]>1:
            print(check(dp[m]))
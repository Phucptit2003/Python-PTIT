import math
def check(s):
    t=len(s)
    for i in range(2,int(t**0.5)+1,1):
        if t%i==0:
            return False
    return t>1

def check1(i):
    if int(i)==2 or int(i)==3 or int(i)==5 or int(i)==7:
        return True
    else:
        return False
    
            

test=int(input())
for _ in range(test):
    s=str(input())
    if check(s)==False:
        print("NO")
    else:   
        cntnto=0
        cnt=0
        for i in s:
            if check1(i)==False:
                cnt+=1
            else:
                cntnto+=1
        if cntnto>cnt:
            print("YES")
        else:
            print("NO")
                
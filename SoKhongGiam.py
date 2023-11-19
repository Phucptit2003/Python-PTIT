test=int(input())
for _ in range(test):
    s=str(input())
    check=False
    for i in range(len(s)-1):
        if(int(s[i])>int(s[i+1])):
            check=True
            break
    if check==False: 
        print("YES")
    else:
        print("NO")
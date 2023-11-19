test=int(input())
for _ in range(test):
    s1=str(input())
    s2=""
    for i in range(len(s1)-1,-1,-1):
        s2+=s1[i]
    check=False
    l=len(s1)
    for i in range(1,l):
        if abs(ord(s1[i])-ord(s1[i-1]))!=abs(ord(s2[i])-ord(s2[i-1])):
            check=True
            break
    if check==False:
        print("YES")
    else:
        print("NO")
    
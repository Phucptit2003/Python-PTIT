test=int(input())
for _ in range(test):
    s=str(input())
    so=[]
    chu=[]
    for i in range(len(s)):
        if s[i]>='A' and s[i]<='Z':
            chu.append(s[i])
        else:
            so.append(int(s[i]))
    chu.sort()
    for i in range(len(chu)):
        print(chu[i],end="")
    print(sum(so))
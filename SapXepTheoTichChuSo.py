def mul(s):
    tich=1
    for i in s:
        tich*=int(i)
    return tich

test=int(input())
for _ in range(test):
    n=int(input())
    tmp =input().split()
    tmp.sort(key=lambda s: (mul(s),int(s)))
    print(*tmp)


test=int(input())
for _ in range(test):
    n=int(input())
    tmp =input().split()
    tmp.sort(key=lambda s: (sum(int(i) for i in s),int(s)))
    print(*tmp)
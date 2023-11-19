arr=[int(i) for i in input().split()]
tmp=[]
for i in arr:
    if i not in tmp:
        tmp.append(i)
print(*tmp)
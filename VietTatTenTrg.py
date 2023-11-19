def check(i):
    if i[0:]=="and":
        return False
    if i[0:]=="of":
        return False
    if i[0:]=="in":
        return False
    return True

test=int(input())
for _ in range(test):
    s=input()
    arr=s.split()
    res=""
    for i in arr:
        if check(i):
            res+=i[0]
    print(res,s)
            
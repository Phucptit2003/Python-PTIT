

test=int(input())
for _ in range(test):
    Tong=sum(int(i) for i in input())
    if Tong%3==0:
        print("YES")
    else:
        print("NO")
    
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
A=set(a)
B=set(b)
intersection = sorted(A & B)

# Tìm hiệu A - B
difference_a_b = sorted(A - B)

# Tìm hiệu B - A
difference_b_a = sorted(B - A)


print(*intersection)
print(*difference_a_b)
print(*difference_b_a)







import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def is_divisible(A, B):
    # Tính GCD của các số trong dãy A và dãy B
    lcm_A = A[0]
    for num in A[1:]:
        lcm_A = lcm(lcm_A, num)

    gcd_B = B[0]
    for num in B[1:]:
        gcd_B = gcd(gcd_B, num)

    # Kiểm tra xem GCD của dãy A chia hết cho GCD của dãy B hay không
    if lcm_A % gcd_B == 0:
        return True
    else:
        return False

# Đọc n và m từ input
n, m = map(int, input().split())

# Đọc dãy số a từ input
A = list(map(int, input().split()))

# Đọc m dãy số b từ input
queries = []
for _ in range(m):
    b = list(map(int, input().split()))
    queries.append(b)

# Tính số bộ dãy số b[] thỏa mãn yêu cầu
count = 0
results = []
i=0
for query in queries:
    i+=1
    if is_divisible(A, query):
        count += 1
        results.append(i)

# In ra kết quả
print(count)
for result in results:
    print(result,end=" ")

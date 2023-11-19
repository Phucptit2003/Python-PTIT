def update(bit, idx, val):
    while idx < len(bit):
        bit[idx] += val
        idx += idx & -idx

def query(bit, idx):
    res = 0
    while idx > 0:
        res += bit[idx]
        idx -= idx & -idx
    return res

def find_initial_rank(N, q, counts, queries):
    bit = [0] * (N + 1)
    for i in range(1, N):
        update(bit, i + 1, 1)
    
    result = []
    for query in queries:
        left, right = 1, N
        while left < right:
            mid = (left + right) // 2
            if query <= query(bit, mid):
                right = mid
            else:
                left = mid + 1
        result.append(left)
        update(bit, left, -1)
    
    return result

# Đọc input
N, q = map(int, input().split())
counts = list(map(int, input().split()))
queries = [int(input()) for _ in range(q)]

# Tính và in ra kết quả
result = find_initial_rank(N, q, counts, queries)
for res in result:
    print(res)

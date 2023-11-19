import heapq

def min_cost(N, K, A):
    heapq.heapify(A)
    cost = 0

    while len(A) > 1:
        selected_elements = [heapq.heappop(A) for _ in range(min(K, len(A)))]
        new_element = sum(selected_elements)
        max_selected = max(selected_elements)
        min_selected=min(selected_elements)

        cost += (K - 1) * (max_selected-min_selected)
        heapq.heappush(A, new_element)

    return A[0], cost

# Đọc input từ bàn phím
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Tính và in ra kết quả
result, total_cost = min_cost(N, K, A)
print(result)
print(total_cost)

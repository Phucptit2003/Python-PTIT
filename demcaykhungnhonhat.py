import heapq

MOD = 10**9 + 7

def prim(N, edges):
    graph = {i: [] for i in range(1, N + 1)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    visited = [False] * (N + 1)
    min_heap = [(0, 1)]  # (trọng số, đỉnh)
    total_weight = 0
    num_trees = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue

        visited[u] = True
        total_weight += weight
        num_trees += 1

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))

    return total_weight % MOD, num_trees % MOD

# Hàm main để đọc input và in kết quả
if __name__ == "__main__":
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    total_weight, num_trees = prim(N, edges)
    print(total_weight, num_trees)

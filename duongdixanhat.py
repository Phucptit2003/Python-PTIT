from collections import defaultdict, deque

def bfs(graph, start):
    queue = deque([(start, 0)])
    visited = set([start])
    farthest_node = start
    max_distance = 0

    while queue:
        node, distance = queue.popleft()
        if distance > max_distance:
            farthest_node = node
            max_distance = distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return farthest_node, max_distance

def find_farthest_nodes(N, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)


    start = 1  
    farthest_node, _ = bfs(graph, start)

    # Tìm điểm xa nhất từ điểm xa nhất trên
    _, max_distance = bfs(graph, farthest_node)

    return max_distance

N = int(input())
edges = []
for _ in range(N - 1):
    u, v = map(int, input().split())
    edges.append((u, v))

result = find_farthest_nodes(N, edges)
print(result)

def is_star_graph(n, edges):
    # Tạo một danh sách kề để lưu các đỉnh kề với mỗi đỉnh
    adjacency_list = [[] for _ in range(n)]
    
    # Tính bậc của từng đỉnh
    degrees = [0] * n
    
    for u, v in edges:
        adjacency_list[u - 1].append(v - 1)
        adjacency_list[v - 1].append(u - 1)
        degrees[u - 1] += 1
        degrees[v - 1] += 1
    
    # Tìm đỉnh có bậc lớn nhất
    max_degree_vertex = max(range(n), key=lambda x: degrees[x])
    
    # Kiểm tra xem đỉnh có bậc lớn nhất có bậc bằng N - 1 và tất cả các đỉnh khác có bậc bằng 1 không
    if degrees[max_degree_vertex] == n - 1 and all(degrees[i] == 1 for i in range(n) if i != max_degree_vertex):
        return "Yes"
    else:
        return "No"

# Đọc số đỉnh N
n = int(input())

# Đọc danh sách các cạnh
edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))

result = is_star_graph(n, edges)
print(result)

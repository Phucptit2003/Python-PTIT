def DFSUtil(graph, v, visited, component):
    visited[v] = True
    component.append(v)

    for i in graph[v]:
        if not visited[i]:
            DFSUtil(graph, i, visited, component)

def findConnectedComponents(graph, vertices):
    visited = [False] * vertices
    components = []

    for v in range(vertices):
        if not visited[v]:
            component = []
            DFSUtil(graph, v, visited, component)
            components.append(component)

    return components


# Hàm chính
def main():
    n, m = map(int, input().split())  # Nhập số đỉnh và số cạnh
    graph = [[] for _ in range(n + 1)]  # Khởi tạo đồ thị với kích thước n + 1

    # Nhập các cạnh
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    components = findConnectedComponents(graph, n + 1)

    # In kết quả
    print(len(components))  # In số thành phần liên thông

    for component in components:
        print(len(component), end=" ")  # In số đỉnh của thành phần liên thông
        print(*component)  # In các đỉnh của thành phần liên thông


if __name__ == "__main__":
    main()

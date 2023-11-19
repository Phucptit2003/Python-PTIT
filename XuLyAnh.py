# Hàm để làm mịn ảnh bằng phép tích chập với kernel
def smooth_image(image, kernel_size):
    n, m = len(image), len(image[0])
    k = (kernel_size - 1) // 2
    smoothed_image = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            total = 0
            for u in range(-k, k + 1):
                for v in range(-k, k + 1):
                    if 0 <= i + u < n and 0 <= j + v < m:
                        total += image[i + u][j + v]
            smoothed_image[i][j] = total // (kernel_size * kernel_size)

    return smoothed_image

# Đọc số lượng bộ test
T = int(input())

for _ in range(T):
    # Đọc kích thước và ma trận ảnh
    N, M, L = map(int, input().split())
    image = [list(map(int, input().split())) for _ in range(N)]

    # Làm mịn ảnh
    smoothed_image = smooth_image(image, L)

    # In kết quả
    for row in smoothed_image:
        print(*row)

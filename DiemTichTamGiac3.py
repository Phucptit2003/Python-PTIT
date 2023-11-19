import numpy as np

def area(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

def solve(N, triangles):
    grid = np.zeros((1000, 1000), dtype=float)

    for triangle in triangles:
        x1, y1, x2, y2, x3, y3 = triangle
        min_x, max_x = min(x1, x2, x3), max(x1, x2, x3)
        min_y, max_y = min(y1, y2, y3), max(y1, y2, y3)

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                if x1 <= x <= x2 and y1 <= y <= y2 and x1 <= x <= x3 and y1 <= y <= y3:
                    grid[x][y] += area(x1, y1, x2, y2, x3, y3)

    total_area = np.sum(grid)
    print("{:.6f}".format(total_area))

if __name__ == "__main__":
    N = int(input())
    triangles = [list(map(int, input().split())) for _ in range(N)]
    solve(N, triangles)
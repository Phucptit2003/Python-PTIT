import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calculate_entropy(p, q, r):
    """
    Tính Entropy của nguồn rời rạc với xác suất p, q, r
    """
    probabilities = np.array([p, q, r])
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

def calculate_entropy_grid(p_values, q_values, r_values):
    """
    Tính Entropy cho tất cả các bộ giá trị của p, q, r
    và vẽ đồ thị 3D tập giá trị kết quả
    """
    p_grid, q_grid, r_grid = np.meshgrid(p_values, q_values, r_values, indexing='ij')
    entropy_grid = calculate_entropy(p_grid, q_grid, r_grid)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(p_grid, q_grid, entropy_grid, cmap='viridis')
    ax.set_xlabel('p')
    ax.set_ylabel('q')
    ax.set_zlabel('Entropy')
    plt.title('Đồ thị 3D của Entropy')
    plt.show()

def calculate_entropy_max(p0_values, p_values, q_values):
    """
    Tính Entropy tương ứng với mỗi giá trị p0
    và tìm giá trị cực đại của Entropy (Hp0_max)
    Vẽ tập giá trị Hp0_max theo p0
    """
    entropy_max_values = []

    for p0 in p0_values:
        entropy_values = []

        for p in p_values:
            for q in q_values:
                r = p0
                entropy = calculate_entropy(p, q, r)
                entropy_values.append(entropy)

        entropy_max = np.max(entropy_values)
        entropy_max_values.append(entropy_max)

    plt.plot(p0_values, entropy_max_values)
    plt.xlabel('p0')
    plt.ylabel('Hp0_max')
    plt.title('Tập giá trị Hp0_max theo p0')
    plt.show()

# Giá trị p, q, r cho nguồn rời rạc
p = 0.3
q = 0.4
r = 0.3

# Tính và in Entropy của nguồn
entropy = calculate_entropy(p, q, r)
print(f"Entropy của nguồn: {entropy}")

# Các giá trị p, q, r thay đổi
p_values = np.linspace(0, 1, 50)
q_values = np.linspace(0, 1, 50)
r_values = np.linspace(0, 1, 50)

# Tính Entropy cho tất cả các bộ giá trị và vẽ đồ thị 3D
calculate_entropy_grid(p_values, q_values, r_values)

# Các giá trị p, q cố định, r thay đổi
p_values_fixed = np.linspace(0, 1, 50)
q_values_fixed = np.linspace(0, 1, 50)
r_values_fixed = np.linspace(0, 1, 50)

# Tính và vẽ tập giá trị Hp0_max theo p0
calculate_entropy_max(r_values_fixed, p_values_fixed, q_values_fixed)

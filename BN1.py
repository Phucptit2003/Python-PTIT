import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Tính entropy của nguồn
#def entropy(p, q, r):
#    H = -p * np.log2(p) - q * np.log2(q) - r * np.log2(r)
#    return H
def entropy(p, q, r):
    H = -np.sum(np.multiply([p, q, r], np.log2([p, q, r])))
    return H

# Vẽ đồ thị 3D tập giá trị entropy
def plot_entropy():
    p_range = np.arange(0.01, 1, 0.01)
    q_range = np.arange(0.01, 1, 0.01)
    r_range = np.arange(0.01, 1, 0.01)
    P, Q, R = np.meshgrid(p_range, q_range, r_range)
    H = entropy(P, Q, R)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
   # ax.plot_surface(P, Q, H,  cmap='viridis')  
 #   ax = fig.gca(projection='3d')

  #  ax.plot_trisurf(P, Q, H, linewidth=0.2, antialiased=True)
    ax.set_xlabel('p')
    ax.set_ylabel('q')
    ax.set_zlabel('Entropy')
    plt.show()

# Tính entropy tối đa với một giá trị r cho trước
def max_entropy_with_fixed_r(p0):
    p_range = np.arange(0.01, 1, 0.01)
    q_range = np.arange(0.01, 1, 0.01)
    H_max = 0
    for p in p_range:
        for q in q_range:
            r = p0
            H = entropy(p, q, r)
            if H > H_max:
                H_max = H
    return H_max

# Vẽ tập giá trị entropy tối đa theo p0
def plot_max_entropy_with_fixed_r():
    p0_range = np.arange(0.01, 1, 0.01)
    Hp0_max = []
    for p0 in p0_range:
        H_max = max_entropy_with_fixed_r(p0)
        Hp0_max.append(H_max)
    plt.plot(p0_range, Hp0_max)
    plt.xlabel('p0')
    plt.ylabel('Hp0_max')
    plt.show()

# Thực hiện nhiệm vụ 1
p = 0.4
q = 0.3
r = 0.3
H = entropy(p, q, r)
print(f'Entropy của nguồn là: {H:.4f}')

# Thực hiện nhiệm vụ 2
plot_entropy()

# Thực hiện nhiệm vụ 3
plot_max_entropy_with_fixed_r()

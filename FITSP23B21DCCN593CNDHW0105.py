#  Lê Đình Phúc
# B21DCCN593
# 05
# Lý thuyết thông tin
# 05
import numpy as np
import matplotlib.pyplot as plt

def calculate_greismer_bound(n, k):
    """
    Tính toán giới hạn Greismer cho mã khối tuyến tính
    """
    return n - k + 1

def calculate_plotkin_bound(n, k):
    """
    Tính toán giới hạn Plotkin cho mã khối tuyến tính
    """
    return 2 * (n - k + 1)

def calculate_hamming_bound(d):
    """
    Tính toán giới hạn Hamming cho mã khối tuyến tính
    """
    return 2 * d - 1

def plot_limits(n, k):
    """
    Vẽ đồ thị các giới hạn Greismer, Plotkin và Hamming
    """
    k_values = np.arange(1, k+1)
    greismer_values = calculate_greismer_bound(n, k_values)
    plotkin_values = calculate_plotkin_bound(n, k_values)
    hamming_values = calculate_hamming_bound(k_values)

    plt.plot(k_values, greismer_values, label="Greismer")
    plt.plot(k_values, plotkin_values, label="Plotkin")
    plt.plot(k_values, hamming_values, label="Hamming")
    plt.xlabel("k")
    plt.ylabel("Giới hạn")
    plt.title("Các giới hạn Greismer, Plotkin và Hamming")
    plt.legend()
    plt.show()

# Tham số n và k của mã khối tuyến tính
n = 9
k = 7

# Tính toán và in các giá trị giới hạn
greismer_limit = calculate_greismer_bound(n, k)
plotkin_limit = calculate_plotkin_bound(n, k)
hamming_limit = calculate_hamming_bound(n - k)

print(f"Giới hạn Greismer: {greismer_limit}")
print(f"Giới hạn Plotkin: {plotkin_limit}")
print(f"Giới hạn Hamming: {hamming_limit}")

# Vẽ đồ thị các giới hạn
plot_limits(n, k)

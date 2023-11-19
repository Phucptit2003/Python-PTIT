class SoPhuc:
    def __init__(self, a, b):
        self.real = a
        self.imaginary = b

    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imaginary + other.imaginary
        return SoPhuc(real_sum, imag_sum)

    def __mul__(self, other):
        real_product = (self.real * other.real) - (self.imaginary * other.imaginary)
        imag_product = (self.real * other.imaginary) + (self.imaginary * other.real)
        return SoPhuc(real_product, imag_product)

    def square(self):
        return self * self

# Hàm để đọc một số phức từ đầu vào
def read_complex_number():
    a, b, c, d = map(int, input().split())
    return SoPhuc(a, b), SoPhuc(c, d)

# Hàm main
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A, B = read_complex_number()
        C = (A + B) * A
        D = (A + B).square()

        print(str(C.real)+" + "+str(C.imaginary)+"i, " + str(D.real)+" + "+str  (D.imaginary)+"i")

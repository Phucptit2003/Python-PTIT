import math

def is_minimal(poly):
    n = len(poly)
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors = [i, n // i]
            for factor in factors:
                factor_poly = [0] * factor
                for j in range(n):
                    if poly[j] == 1 and (j % factor) != (factor - 1):
                        break
                    if j == n - 1:
                        return False
    return True

def list_minimal_polynomials(k):
    polynomials = []
    for i in range(2**k):
        poly = list(bin(i)[2:].zfill(k))
        poly = [int(x) for x in poly]
        if is_minimal(poly):
            polynomials.append(poly)
    return polynomials


def is_irreducible(poly):
    return is_minimal(poly)


def factorize_polynomial(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
    factors = sorted(set(factors))
    return factors


def list_distinct_factors(n):
    factors = factorize_polynomial(n)
    distinct_factors = []
    for factor in factors:
        poly = [0] * factor
        poly[-1] = 1
        if is_irreducible(poly):
            distinct_factors.append(poly)
    return distinct_factors

k = int(input("Nhập(k): "))


minimal_polynomials = list_minimal_polynomials(k)
print("Minimal polynomials of degree", k, ":")
for poly in minimal_polynomials:
    print(poly)


poly = list(input("Nhập các hệ số đa thức (e.g., 1010110): "))
poly = [int(x) for x in poly]
if is_irreducible(poly):
    print("Đa thức bất khả quy.")
else:
    print("Đa thức có thể rút gọn.")


n = int(input("Nhập n: "))
factors = factorize_polynomial(n)
print("Đa thức x^", n, "+ 1:")
for factor in factors:
    print("x ^", factor, "+ 1")


distinct_factors = list_distinct_factors(n)
print("Các nhân tử phân biệt x^", n, "+ 1:")
for factor in distinct_factors:
    print(factor)

# Lê Đình Phúc
# B21DCCN593
# 05
# Lý thuyết thông tin
# 07
def generate_subsets(elements):
    subsets = [[]]
    for element in elements:
        subsets += [subset + [element] for subset in subsets]
    return subsets

def list_all_test_sums(code):
    nL = code['nL']
    poly = code['poly']
    subsets = generate_subsets(poly)
    test_sums = []
    for subset in subsets:
        test_sum = sum(subset) % nL
        if test_sum not in test_sums:
            test_sums.append(test_sum)
    return test_sums

def check(code):
    nL = code['nL']
    poly = code['poly']
    subsets = generate_subsets(poly)
    for subset in subsets:
        subset_sum = sum(subset) % nL
        if subset_sum == 0:
            return False
    return True

def check1(code):
    nL = code['nL']
    poly = code['poly']
    isGPoly = code['isGPoly']
    subsets = generate_subsets(poly)
    for subset in subsets:
        subset_sum = sum(subset) % nL
        if subset_sum == 0 and isGPoly:
            return False
    return True

# Example code
code = {
    'codename':'D',
    'nL':8,
    'poly':[1,2,5],
    'isGPoly':1
}

print("Các tổng kiểm tra có thể:", list_all_test_sums(code))
print("Mã vòng tuyến tính có khả năng trực giao đầy đủ:", check(code))
print("Mã vòng tuyến tính có khả năng trực giao:", check1(code))

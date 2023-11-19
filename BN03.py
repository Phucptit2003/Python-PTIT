#  Lê Đình Phúc
# B21DCCN593
# 05
# Lý thuyết thông tin
# 03
def check_uniform(codewords):
    """
    Kiểm tra xem danh sách các từ mã có đều không
    """
    lengths = set(len(word) for word in codewords)
    return len(lengths) == 1

def check_linear_block_code(codewords):
    """
    Kiểm tra xem bộ mã có phải là mã khối tuyến tính không
    """
    codeword_length = len(codewords[0])
    for i in range(len(codewords)):
        if len(codewords[i]) != codeword_length:
            return False
    return True

def check_basis(codewords):
    """
    Kiểm tra xem danh sách các từ mã có tạo thành hệ cơ sở không
    """
    return len(codewords) == len(set(codewords))

def check_cyclic_linear_code(codewords):
    """
    Kiểm tra xem bộ mã có phải là mã vòng (mã cyclic) tuyến tính không
    """
    codeword_length = len(codewords[0])
    for i in range(1, len(codewords)):
        if codewords[i] != codewords[i-1][1:] + codewords[i-1][0]:
            return False
    return True

def check_permutation(code1, code2):
    """
    Kiểm tra xem hai bộ mã có phải là một (là hoán vị của nhau) không
    """
    return sorted(code1) == sorted(code2)

# Bộ mã đã cho
code = {
    'codename': 'C',
    'codewords': ['1', '01', '001', '000']
}

# Thực hiện kiểm tra các đặc tính của bộ mã
is_uniform = check_uniform(code['codewords'])
is_linear_block_code = check_linear_block_code(code['codewords'])
is_basis = check_basis(code['codewords'])
is_cyclic_linear_code = check_cyclic_linear_code(code['codewords'])

# In kết quả
print(f"Các đặc tính cơ bản của bộ mã '{code['codename']}':")
print(f"Đều: {'Có' if is_uniform else 'Không'}")
print(f"Suy biến: {'Có' if not is_linear_block_code else 'Không'}")
if not is_linear_block_code:
    print("Minh họa suy biến: Bộ mã không phải là mã khối tuyến tính.")
print(f"Giải mã duy nhất: {'Có' if is_basis else 'Không'}")
if not is_basis:
    print("Minh họa giải mã không duy nhất: Bộ mã không tạo thành hệ cơ sở.")
print(f"Tính prefix: {'Có' if is_linear_block_code else 'Không'}")
if not is_linear_block_code:
    print("Minh họa không prefix: Bộ mã không phải là mã khối tuyến tính.")
print(f"Mã vòng tuyến tính: {'Có' if is_cyclic_linear_code else 'Không'}")

# Kiểm tra hai bộ mã có phải là hoán vị của nhau
code1 = ['1', '01', '001', '000']
code2 = ['000', '01', '001', '1']
is_permutation = check_permutation(code1, code2)

print(f"\nHai bộ mã là hoán vị của nhau: {'Có' if is_permutation else 'Không'}")

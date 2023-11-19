import numpy as np

def find_dmin_from_columns(H):
    n = len(H[0])
    dmin = n
    for i in range(n):
        column_weight = sum([H[j][i] for j in range(len(H))])
        if column_weight < dmin:
            dmin = column_weight
    return dmin

def is_codeword_valid(c, H):
    c = np.array(c)
    H = np.array(H)
    return np.array_equal(np.mod(np.matmul(c, H.T), 2), np.zeros(len(H)))

def list_codewords(H):
    n = len(H[0])
    codewords = []
    for i in range(2**n):
        c = list(bin(i)[2:].zfill(n))
        c = [int(x) for x in c]
        if is_codeword_valid(c, H):
            codewords.append(c)
    return codewords

def find_dmin_definition(H):
    codewords = list_codewords(H)
    dmin = float('inf')
    for i in range(len(codewords)):
        for j in range(i + 1, len(codewords)):
            weight = sum([codewords[i][k] != codewords[j][k] for k in range(len(H[0]))])
            if weight < dmin:
                dmin = weight
    return dmin

def find_dmin_properties(H):
    n = len(H[0])
    dmin = n
    for i in range(n):
        for j in range(i + 1, n):
            if np.array_equal(np.mod(H[:, i] + H[:, j], 2), np.zeros(len(H))):
                weight = sum(H[:, i])
                if weight < dmin:
                    dmin = weight
    return dmin

# Example usage

H = [[1,0,1,1,1,0,0],[0,1,0,1,1,1,0],[0,0,1,0,1,1,1]]
c = [1,1,0,1,0,0]

# Task 1: Find dmin based on the number of columns in H
dmin_columns = find_dmin_from_columns(H)
print("dmin based on columns:", dmin_columns)

# Task 2: Check if a vector is a valid codeword
if is_codeword_valid(c, H):
    print("The vector is a valid codeword.")
else:
    print("The vector is not a valid codeword.")

# Task 3: List all codewords for the code
codewords = list_codewords(H)
print("Codewords:")
for codeword in codewords:
    print(codeword)

# Task 4: Find dmin based on the definition
dmin_definition = find_dmin_definition(H)
print("dmin based on definition:", dmin_definition)

# Task 5: Find dmin based on properties of linear codes
dmin_properties = find_dmin_properties(H)
print("dmin based on properties:", dmin_properties)

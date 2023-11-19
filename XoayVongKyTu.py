def min_steps_to_match(N, S):
    # Đếm số lần xuất hiện của từng kí tự ở vị trí đầu tiên
    char_count = {}
    for i in range(N):
        first_char = S[i][0]
        if first_char not in char_count:
            char_count[first_char] = 1
        else:
            char_count[first_char] += 1
    
    # Kiểm tra nếu có kí tự nào không xuất hiện trong tất cả các xâu
    for char, count in char_count.items():
        if count != N:
            return "NO"
    
    # Tính số bước cần thiết để biến đổi từng xâu
    total_steps = 0
    for i in range(N):
        first_char = S[i][0]
        j = 1
        while S[i][j] != first_char:
            j += 1
        total_steps += j
    
    return total_steps

# Đọc input và thực hiện cho từng test case
T = int(input())
for _ in range(T):
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())
    result = min_steps_to_match(N, S)
    print(result)

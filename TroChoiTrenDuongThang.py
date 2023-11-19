# Hàm tính chi phí tối thiểu để đi đến một điểm trên đường thẳng.
def min_cost_to_reach(destination, cards):
    n = len(cards)
    dp = [float('inf')] * (destination + 1)  # Khởi tạo mảng dp với giá trị vô cực.

    # Bước đi ban đầu từ vị trí 0 có chi phí là 0.
    dp[0] = 0

    for i in range(destination + 1):
        for j in range(n):
            # Nếu có thẻ j có thể sử dụng để đến vị trí i.
            if i >= cards[j][0]:
                dp[i] = min(dp[i], dp[i - cards[j][0]] + cards[j][1])

    return dp[destination]

# Đọc số lượng trò chơi
T = int(input())

for _ in range(T):
    n = int(input())
    ai = list(map(int, input().split()))
    ci = list(map(int, input().split()))

    # Tạo danh sách thẻ với cặp (ai, ci)
    cards = list(zip(ai, ci))

    # Điểm đích là điểm có tọa độ lớn nhất trong danh sách ai.
    destination = max(ai)

    # Tính chi phí tối thiểu để đạt đến điểm đích.
    result = min_cost_to_reach(destination, cards)

    if result == float('inf'):
        print(-1)
    else:
        print(result)

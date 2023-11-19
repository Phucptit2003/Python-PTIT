res=0
def backtrack(bags, max_weight, current_weight, current_bags):
    if current_weight > max_weight:  # Kiểm tra điều kiện dừng
        return

    for i in range(len(bags)):
        new_weight = current_weight + bags[i]
        if new_weight <= max_weight:  # Kiểm tra xem có thể chở thêm bao ngô không
            current_bags.append(bags[i])
            backtrack(bags, max_weight, new_weight, current_bags)
            current_bags.pop()  # Quay lui
        else:
            if new_weight-bags[i]>res:
                res=new_weight-bags[i]
    print(res)
# Đọc input
n,max_weight  = map(int, input().split())
bags = list(map(int, input().split()))

# Gọi hàm backtrack
backtrack(bags, max_weight, 0, [])

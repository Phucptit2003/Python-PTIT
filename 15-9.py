def sum_of_integers_in_range(l, r):
    # Tính tổng từ 1 đến r
    sum_up_to_r = (r + 1) // 2
    
    # Tính tổng từ 1 đến l-1
    sum_up_to_l_minus_1 = (l - 1) // 2 if l > 1 else 0
    
    # Tính tổng các số lẻ từ l đến r
    result = sum_up_to_r - sum_up_to_l_minus_1
    
    return result
test=int(input())
for _ in range(test):
    l,r=map(int,input().split())
    tong=sum_of_integers_in_range(l,r)
    print(tong)
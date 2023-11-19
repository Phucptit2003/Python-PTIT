def can_transform_to_full_string(S, K):
    khac = set(S)
    thieu = 26 - len(khac)
    
    if thieu <= 0:
        return "YES"  
    
    if K >= thieu:
        return "YES" 
    
    return "NO"

T = int(input())  
for _ in range(T):
    S = input()  
    K = int(input()) 
    result = can_transform_to_full_string(S, K)
    print(result)

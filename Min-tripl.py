
def find_min_triplet_sum(arr):  
    tmp=[]
    tmp.append(arr[0])
    tmp.append(arr[1])
    tmp.append(arr[2])
    for i in range(3,len(arr)):
        t=max(tmp)
        if sum(tmp)-t+arr[i]<sum(tmp):
            tmp.remove(t)
            tmp.append(arr[i])      
    
    return sum(tmp)

# Đọc số bộ test
T = int(input())

for _ in range(T):
    N = int(input())
    arr=[int(x) for x in input().split()]
    result = find_min_triplet_sum(arr)
    print(result)

def Count(n, m, k, H, arr):
    cnt = [0] * (m * k + 1)
    for i in range(n):
        dis = abs(H - arr[i])
        cnt[dis % k] += 1
    
    dem = 0
    for i in range(1, m * k, k):
        dem += cnt[i]
    
    return dem

test = int(input())
for _ in range(test):
    n, m, k, H = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = Count(n, m, k, H, arr)
    print(cnt)

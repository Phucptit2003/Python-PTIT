def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        mp = {}
        for i in range(0, n):
            a[i] = a[i] % k
            if a[i] == 0:
                a[i] = k
            if a[i] not in mp:
                mp[a[i]] = []
            mp[a[i]].append(i+1)

        v = sorted(mp.keys(), reverse=True)
        for x in v:
            for y in mp[x]:
                print(y, end=" ")
        print()

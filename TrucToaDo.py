def find_maximum_non_overlapping_segments(segments):
    segments.sort(key=lambda x: x[1])

    count = 0 
    end = -1  

    for segment in segments:
        start, finish = segment
        if start > end:
            count += 1
            end = finish0

    return count


T = int(input())
for _ in range(T):
    N = int(input())
    segments = []

    for _ in range(N):
        x1, x2 = map(int, input().split())
        segments.append((x1, x2))

    result = find_maximum_non_overlapping_segments(segments)
    print(result)


T = int(input())


for _ in range(T):
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    common_elements = []
    i = j = k = 0
    
    while i < N and j < M and k < K:
        if A[i] == B[j] == C[k]:
            common_elements.append(A[i])
            i += 1
            j += 1
            k += 1
        elif A[i] <= B[j] and A[i] <= C[k]:
            i += 1
        elif B[j] <= A[i] and B[j] <= C[k]:
            j += 1
        else:
            k += 1
    
    if common_elements:
        print(*common_elements)
    else:
        print("NO")

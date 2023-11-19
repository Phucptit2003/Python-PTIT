def max_layers(t, testcases):
    results = []
    for i in range(t):
        b, c, h = testcases[i]
        layers_with_cheese_or_ham = min(c, h) * 2
        remaining_bread = b - layers_with_cheese_or_ham // 2
        additional_layers = min(remaining_bread // 2, c + h)
        total_layers = layers_with_cheese_or_ham + additional_layers
        results.append(total_layers)
    return results

# Example usage:
t = int(input())
tmp=[]
for _ in range(test):
    b,c,h=map(int,input().split())
    pair=[b,c,h]
    tmp.append(pair)
    output = max_layers(t, tmp)
    print(output)  # Output: [4, 10, 14]

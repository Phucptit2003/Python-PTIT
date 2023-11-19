def count_different_strings(n, m, s, operations):
    unique_strings = set()
    substrings = [0] * (n + 1)
    for i in range(m):
        l, r = operations[i]
        substrings[l - 1] += 1
        substrings[r] -= 1

    current_count = 0
    for i in range(n):
        current_count += substrings[i]
        if current_count > 0:
            substring = sorted(s[i - current_count:i])
            modified_string = s[:i - current_count] + ''.join(substring) + s[i:]
            unique_strings.add(modified_string)

    return len(unique_strings)

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        s = input()
        operations = [tuple(map(int, input().split())) for _ in range(m)]
        result = count_different_strings(n, m, s, operations)
        print(result)

if __name__ == "__main__":
    main()

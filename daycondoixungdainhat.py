def find_longest_palindromic_substring(s):
    if not s:
        return ""

    # Thêm dấu '#' vào giữa mỗi ký tự trong chuỗi để đảm bảo sẽ luôn có một ký tự giữa các ký tự trong dãy con đối xứng
    modified_s = '#'.join('^{}$'.format(s))
    n = len(modified_s)
    p = [0] * n
    C, R = 0, 0

    for i in range(1, n - 1):
        mirror = 2 * C - i  # Vị trí tương ứng với i (symmetry of i with respect to C)

        if R > i:
            p[i] = min(R - i, p[mirror])

        # Attempt to expand palindrome centered at i
        while modified_s[i + 1 + p[i]] == modified_s[i - 1 - p[i]]:
            p[i] += 1

        # If palindrome centered at i expands past R,
        # adjust center and right boundary
        if i + p[i] > R:
            C, R = i, i + p[i]

    # Find the maximum element in P
    max_length = max(p)
    center_index = p.index(max_length)
    
    # Extract the longest palindromic substring
    longest_palindrome = modified_s[center_index - max_length:center_index + max_length + 1]
    
    # Remove '#' characters from the palindrome string
    longest_palindrome = longest_palindrome.replace("#", "")

    return longest_palindrome


# Test
input_string = str(input())
result = find_longest_palindromic_substring(input_string)
print("Longest Palindromic Substring:", result)

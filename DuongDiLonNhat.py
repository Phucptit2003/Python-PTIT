def max_str(a, b):
    if a > b:
        return a
    return b

def bin_to_dec(s):
    dec = 0
    for i in range(3, 0, -1):
        dec += 2**i * int(s[3 - i])
    return dec

def dec_to_hex(n):
    hex_chars = "0123456789ABCDEF"
    if n == 0:
        return '0'
    tmp = ''
    while n != 0:
        du = n % 16
        n = n // 16
        tmp = hex_chars[du] + tmp
    return tmp

def main():
    n = int(input())
    a = []
    for _ in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    
    c = [['' for _ in range(n + 2)] for _ in range(n + 2)]
    
    for i in range(n + 1):
        for j in range(n + 1):
            c[i][j] = ''
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            c[i][j] = max_str(c[i - 1][j], c[i][j - 1]) + str(a[i - 1][j - 1])
    
    s = c[n][n]
    
    while len(s) > 1 and s[0] == '0':
        s = s[1:]
    
    while len(s) % 4 != 0:
        s = '0' + s
    
    z = -3
    result = ''
    
    for i in range(len(s) // 4):
        z += 4
        x = bin_to_dec(s[z:z + 4])
        result += dec_to_hex(x)
    
    print(result)

if __name__ == "__main__":
    main()

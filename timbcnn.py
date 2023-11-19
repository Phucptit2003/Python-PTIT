def gcd(a, b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

a, b = map(int, input().split())

lcm_result = abs(lcm(a,b))
print( lcm_result)

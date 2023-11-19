def Calculate(n):
    num=10**(2*n)
    result=num-2*10**n+1
    return result
    
n=int(input())
result=Calculate(n)
print(result)
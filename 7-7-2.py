def is_prime(n):
    if n<2: 
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def check(arr):
    b=set()
    array=[]
    for i in arr:
        if is_prime(i)==True:
            b.add(i)
    result=sorted(list(b))
    for i in result:
        array.append(str(i))
    return ' '.join(array)   

n=int(input())
arr=list(map(int,input().split()))
print(check(arr))
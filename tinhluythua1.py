P=  pow(10,9)+7
def Tinh(a,n):
    if n==0:
        return 1
    cnt=Tinh(a,n//2)
    cnt=(cnt*cnt)%P
    if n%2==1:
        return a*cnt%P
    else:
        return cnt%P
a,n=map(int,input().split())
count=Tinh(a,n)
print(count)
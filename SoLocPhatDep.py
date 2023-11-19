def check(s):
    for i in s:
        if i!='8' and i!='6':
            return False
    i=0
    a=[int(i) for i in s]
    for i in range(len(a)):
        if a[0]==8:
            return False
        if a[i]==8 and a[i-1]!=6 and a[i-1]!=8:
            return False
        if i>1 and a[i]==8 and a[i-1]==8 and a[i-2]!=6:
            return False
            
    return True

s=str(input())
if check(s):
    print("YES")
else:
    print("NO")
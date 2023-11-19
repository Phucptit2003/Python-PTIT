n=int(input())
for k in range(n):
    s=str(input())
    t=str(input())
    f=[0]*124
    res=[0]*124
    for i in s:
        f[ord(i)]+=1
    for i in t:
        res[ord(i)]+=1
        
    print(f"Test {k+1}: ",end="")
    
    stop=False
    for i in range(124):
        if f[i]!=res[i]:
            print("NO")
            stop=True
            break
    if stop==False:
        print("YES")
n=int(input())
s=str(input())
cnt=0
dem=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        dem+=1
        if i==len(s)-2:
            cnt+=dem//2
    else:
        cnt+=dem//2
        dem=1
print(cnt)
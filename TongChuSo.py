s=str(input())
tong = 0
if len(s)<2:
    print(1)
    continue
dem=0
if s[0]=='-':
    tong=-1*int(s[1])
    if len(s)==2:
        print(1)
        continue
else:
    tong=int(s[0])+int(s[1])
for i in range(2,len(s)):
    tong+=int(s[i])
s=str(tong)
cnt=1
while len(s)>=2:
    
    
    

    
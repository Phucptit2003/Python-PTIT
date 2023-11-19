s=str(input())
tmp=[]
chiso=[]
for i in range(len(s)):
    if s[i]=='(':
        tmp.append(s[i])
        chiso.append(i+1)
    else:
        tmp.pop()
        print(chiso.pop(),i+1)
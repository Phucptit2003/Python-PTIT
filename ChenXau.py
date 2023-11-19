s1=input()
s2=input()
p=int(input())
res=""
for i in range(p-1):
    res+=s1[i]
for i in range(len(s2)):
    res+=s2[i]
for i in range(p-1,len(s1)):
    res+=s1[i]
print(res)

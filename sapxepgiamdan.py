n=int(input())
s=input()
a=s.split()
a=[int(s) for s in a]
a.sort(reverse=True)
for i in a:
    print(i,end=" ")
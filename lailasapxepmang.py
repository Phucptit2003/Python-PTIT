n=int(input())
astring=input()
arr=astring.split()
arr=[int(astring) for astring in arr]
a=[]
for i in range(1,n-1):
    a.append(arr[i])
a.sort()
b=[]
b.append(arr[0])
for i in a:
    b.append(i)
b.append(arr[n-1])
for i in b:
    print(i,end=" ")

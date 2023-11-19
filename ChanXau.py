s1=input()
s2=input()
p=int(input())
arr1=s1.split()
arr2=s2.split()
for i in range(p-1):
    print(arr1[i],end=" ")
print(*arr2,end="")
for k in range(p-1,len(arr1)):
    print(arr1[k],end=" ")
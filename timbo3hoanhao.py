n=int(input())
string=input()
arr=string.split()
arr=[int(string) for string in arr]
arr.sort()
a,b,c=arr[-3::]
cnt=a*b*c
print(cnt)
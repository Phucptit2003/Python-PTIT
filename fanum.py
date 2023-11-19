n=int(input())
string_input=input()
arr=string_input.split()
arr=[int(string_input) for string_input in arr]
f=[0]*n
for i in range(n):
    f[arr[i]]+=1
count=0
for i in range(n):
    if f[arr[i]]==1:
        count+=1
print(count)
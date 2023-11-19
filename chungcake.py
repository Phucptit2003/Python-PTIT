        
n,v=map(int,input().split())
input_string=input()
arr=input_string.split()
arr=[int(input_string) for input_string in arr]
arr.sort(reverse=True)
i=0
sum=0
while i<n:
    if sum + arr[i]<=v:
        sum+=arr[i]
    else:
        break
print(sum)
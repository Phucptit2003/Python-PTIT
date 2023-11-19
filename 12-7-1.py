input_string=input()
arr=input_string.split()
vector=[]
arr=[int(input_string) for input_string in arr]
n=len(arr)
for i in range(n-1):
    if arr[n-1]==arr[i]:
        vector.append(i+1)
if len(vector)==0:
    print("-1")
else:
    for i in vector:
        print(i,end=" ")
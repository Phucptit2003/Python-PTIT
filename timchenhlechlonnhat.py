n=int(input())
string_input=input()
arr=string_input.split()
arr=[int(string_input) for string_input in arr]
arr.sort()
print(arr[n-1]-arr[0])
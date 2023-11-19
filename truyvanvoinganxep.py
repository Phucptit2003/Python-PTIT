t=int(input())
stack=[]
for _ in range(t):
    input_string=input()
    arr=input_string.split()
    arr=[int(input_string) for input_string in arr]
    if arr[0]==1:
        stack.append(arr[1])
    elif arr[0]==2:
        if len(stack)!=0:
            stack.pop()
    else:
        if len(stack)==0:
            print("Empty!")
        else:
            print(stack[len(stack)-1])
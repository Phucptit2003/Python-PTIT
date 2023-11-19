test=int(input())
queue=[]
i=0
for _ in range(test):
    input_string=input()
    arr=input_string.split()
    arr=[int(input_string) for input_string in arr]
    if arr[0]==1:
        queue.append(arr[1])
    elif arr[0]==2:
        if i<len(queue):
            i+=1
    else:
        if i>=len(queue):
            print("Empty!")
        else:
            print(queue[i])
n=int(input())
for _ in range(n):
    string_inputs=input()
    string_input=string_inputs.split()
    string_input=[str(string_inputs) for string_inputs in string_input]
    stack=[]
    for i in range(len(string_input)):
        if string_input[i]=='(':
            stack.push(string_input[i])
        else:
            if len(stack)!=0:
                stack.pop()
            else:
                stack.push(string_input[i])
    print(len(stack))  
    stack.clear()              
                
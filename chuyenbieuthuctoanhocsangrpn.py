test=int(input())
for _ in range(test):
    s=str(input())
    tmp=[]
    stack=[]
    for i in s:
        if i.isalpha():
            tmp.append(i)
        elif i=='^' or i=='*' or i=='/' or i=='+' or i=='-':
            if len(tmp)>=2:
                tmp.append(stack.pop())
            stack.append(i)
    while len(stack)>0:
        tmp.append(stack.pop())
    for i in range(len(tmp)-1):
        print(tmp[i],end="")
    print(tmp[len(tmp)-1])
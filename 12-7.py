input_string=str(input())
num=0
n=len(input_string)

vector=[]
check=0
for i in range(n):
    if input_string[i].isdigit() or input_string[i+1].isdigit():
        if input_string[i].isdigit():
            num=num*10+int(input_string[i])
        if i==n-1:
            vector.append(num)
    elif  input_string[i]=='+' or  input_string[i]=='-' or  input_string[i]=='*'or  input_string[i]=='/':
        t=input_string[i]
        vector.append(num)
        num=0

if t=='+':
    result=vector[0]+vector[1]
elif t=='-':
    result=vector[0]-vector[1]
elif t=='*':
    result=vector[0]*vector[1]
else:
    if vector[1]==0:
        print("Math Error")
        check=1
    else:
        result=vector[0]/vector[1]
if check==0:
    print("{:.2f}".format(result))
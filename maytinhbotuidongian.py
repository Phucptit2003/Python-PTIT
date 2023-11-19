
input_string=input()
arr_string=input_string.split()
arr_string=[str(input_string) for input_string in arr_string]
num=[]
check=0
for i in arr_string:
    if i.isdigit():
        num.append(int(i))
    else:
        t=i
if t=='+':
    result=num[0]+num[1]
elif t=='-':
    result=num[0]-num[1]
elif t=='*':
    result=num[0]*num[1]
else:
    if num[1]==0:
        print("Math Error")
        check=1
    else:
        result=num[0]/num[1]
if check==0:
    print("{:.2f}".format(result))
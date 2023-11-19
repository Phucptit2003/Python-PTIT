n=int(input())
input_string=input()
arr=input_string.split()
arr=[int(input_string) for input_string in arr]
cnt=0
cnt1=0
check=False
for i in arr:
    if i<0:
        cnt+=1
    elif i>0:
        cnt1+=1
    else:
        check=True
        print("-1")
        break
if check==False:
    print(min(cnt,cnt1))
        
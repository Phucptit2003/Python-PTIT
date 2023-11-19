n=int(input())
s=str(input())
input_string=input()
arr=input_string.split()
arr=[int(input_string) for input_string in arr]
char = 'a'
for i in s:
    if i.isalpha():
        arr[ord(i)-97]-=1

tmp=[]
for i in s:
    if i=='?':
        for j in range(len(arr)):
            if arr[j]>0:
                tmp.append(chr(j+97))
                arr[j]-=1
                break
    else:
        tmp.append(i)
check=True
for i in arr:
    if i>0:
        check=False
        print("-1")
        break
if check==True:
    for i in tmp:
        if i=='?':
            check=False
            print("-1")
if check==True:
    for i in tmp:
        print(i,end="")
   
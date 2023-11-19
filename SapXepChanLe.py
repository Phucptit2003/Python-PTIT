n=int(input())
arr=[]
while len(arr)<n:
    tmp=[int(i) for i in input().split()]
    for i in tmp:
        arr.append(i) 
chan=[]
le=[]
for num in arr:
    if num%2==0:
        chan.append(num)
    else:
        le.append(num)
chan.sort()
le.sort(reverse=True)
j=k=0
for num in arr:
    if num%2==0:
        print(chan[j],end=" ")
        j+=1
    else:
        print(le[k],end=" ")
        k+=1
    

            
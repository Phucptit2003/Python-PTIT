test=int(input())
for _ in range(test):
    s1=str(input())
    s2=str(input())
    l1=len(s1)
    l2=len(s2)
    arr1=[0]*100
    arr2=[0]*100
    for i in range(l1):
        arr1[ord(s1[i])]+=1
    for i in range(l2):
        arr2[ord(s2[i])]+=1
    cnt=0
    for i in range(65,91):
        if arr1[i]>0 and arr2[i]>0:
            cnt+=1
    print(cnt)
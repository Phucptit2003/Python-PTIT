test=int(input())
for _ in range(test):
    n=int(input())
    arr=[int(i) for i in input().split()]
    st=[]
    res=[0]*n
    for i in range(n):
        while(len(st)>0 and arr[i] >= arr[st[-1]]):
            st.pop()
        if len(st)==0: 
            res[i]=i+1
        else:
            res[i]=i-st[-1]
        st.append(i)
    for i in res:
        print(i,end=" ")
    print()
n=int(input())
cnt=[]
tutuyet=[]
lucbat=[]
for i in range(n):
    s=input()
    arr=s.split()
    if len(arr)==6 or len(arr)==8:
        lucbat.append(s)
        if i==n-1:
            cnt.append(1)       
        tutuyet=[]
    elif len(arr)==7:
        tutuyet.append(s)
        if len(lucbat)!=0:
            cnt.append(1)
        lucbat=[]
    if len(tutuyet)==4:
        cnt.append(2)
        tutuyet=[] 
print(len(cnt))
for x in cnt:
    print(x)
    
        
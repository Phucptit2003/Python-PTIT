def sort_sv(arr):
    arr.sort(key=lambda x: (-x[1],x[2],x[0]))

test=int(input())
arr=[]
for _ in range(test):
    name=input().strip()
    a,b=map(int,input().split())
    arr.append((name,a,b))
sort_sv(arr)
for i in arr:
    print(i[0]+" "+str(i[1])+" "+str(i[2]))

    
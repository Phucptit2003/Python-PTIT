n=int(input())
a=[float(i) for i in input().split()]
maxx,minn=max(a),min(a)
lst=[]
for i in a:
    if i !=minn and i!= maxx:
        lst.append(i)
print("{:.2f}".format(sum(lst)/len(lst)))
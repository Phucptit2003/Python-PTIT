def QL(a):
    result=[]
    backtrack(a,[],result)
    return result

def backtrack(a,path,result):
    if not a:
        result.append(path)
        return
     
    for i in range(len(a)):
        next_num=a[i]
        remain_num=a[:i]+a[i+1:]
        backtrack(remain_num,path+[next_num],result)

n=int(input())
a=[0]*(n)
for i in range(n):
    a[i]=i+1
v=QL(a)
vector_string=""
for i in v:
    num_string=' '.join(str(v) for v in i)
    vector_string+=num_string+"\n"
print(vector_string)

n=int(input())
i=2
vector=[]
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        time=0   
        while n%i==0:
            time+=1
            n//=i
        pair=(i,time)
        vector.append(pair)
    else:
        i+=1
if n>1:
    pair=(n,1)
    vector.append(pair)
print(len(vector))
vector_string=""
for pair in vector:
    pair_string=' '.join(str(vector) for vector in pair)
    vector_string+=pair_string+'\n'
print(vector_string)
        
            
        
    
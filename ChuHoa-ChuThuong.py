s=str(input())
sum_thuong=0
sum_hoa=0
for i in s:
    if i>='a' and i<='z':
        sum_thuong+=1
    else:
        sum_hoa+=1
if sum_thuong>=sum_hoa:
    tnp=s.lower()
else:
    tnp=s.upper()
print(tnp)   
n = int(input())
s = 1/n
for i in range(2,n):
    s+=1/i
print("{:.4f}".format(s))
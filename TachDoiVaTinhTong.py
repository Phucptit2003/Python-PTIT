s=str(input())

while len(s)>1:
    left_sum=0
    right_sum=0
    for i in range(0,len(s)//2):
        left_sum=left_sum*10+int(s[i])
 
    for i in range(len(s)//2,len(s)):
        right_sum=right_sum*10+int(s[i])

    tong=left_sum+right_sum
    s=str(tong)
    print(s)

    
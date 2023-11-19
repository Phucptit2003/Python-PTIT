P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    String=input()
    if String=='0':
       break
    k,s=String.split()
    k=int(k)
    res="";
    for i in s:
        j=P.find(i)
        res+=P[(j+k)%28]
    print(res[::-1])
import re

s=''
regex=r'[.!?]'
while True:
    try:
        s+=input()
    except EOFError:
        break

s=re.split(regex,s)

for i in s:
    x=i.strip().lower().split()
    if len(x)>0:
        x[0]=x[0].title()
        print(*x)
def check(s):
    tmp=s.lower()
    if tmp[-3:]==".py":
        return True
    else:
        return False

s=str(input())
if check(s):
    print("yes")
else:
    print("no")
def ChuHoa(i):
    if i>='A' and i<='Z':
        return True
    return False

def ChuThuong(i):
    if i>='a' and i<= 'z':
        return True
    return False

s=str(input())
cnt_Hoa=0
cnt_Thg=0
for i in s:
    if ChuHoa(i):
        cnt_Hoa+=1
    elif ChuThuong(i):
        cnt_Thg+=1
print(cnt_Hoa,cnt_Thg)
        
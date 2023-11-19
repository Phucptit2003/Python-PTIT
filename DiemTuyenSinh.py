class SinhVien:

    def __init__(self,stt,name,diemthi,dantoc,khuvuc):
        self.stt=stt
        self.name=self.ChuanHoa(name)
        self.diemthi=diemthi
        self.dantoc=dantoc
        self.khuvuc=khuvuc
        self.tongdiem=0
        self.trangthai=""
    
    def ChuanHoa(self,name):
        arr=name.split()
        s=""
        for i in range(len(arr)):
            s+=arr[i][0].upper()+arr[i][1:].lower()
            if i!=len(arr)-1:
                s+=" "
        return s
    def TongDiem(self):
        diemcong=0
        if self.khuvuc==1:
            diemcong+=1.5
        elif self.khuvuc==2:
            diemcong+=1
        if self.dantoc!="Kinh":
            diemcong+=1.5
        return self.diemthi+diemcong
    
    def TrangThai(self):
        if self.tongdiem<20.5:
            self.trangthai="Truot"
        else :
            self.trangthai="Do"
        return self.trangthai

    def __lt__(self,other):
        self.tongdiem=self.TongDiem()
        other.tongdiem=other.TongDiem()
        if self.tongdiem==other.tongdiem:
            return self.stt<other.stt
        return self.tongdiem>other.tongdiem
    

n=int(input())
danhsach=[]
for i in range(n):
    name=input()
    diemthi = float(input())
    dantoc=str(input())
    khuvuc=int(input())
    ts=SinhVien("TS{:02d}".format(i+1),name,diemthi,dantoc,khuvuc)
    danhsach.append(ts)
danhsach.sort()
for i in danhsach:
    tongdiem=i.TongDiem()
    trangthai=i.TrangThai()
    print(f"{i.stt} {i.name} {tongdiem:.1f} {trangthai}")
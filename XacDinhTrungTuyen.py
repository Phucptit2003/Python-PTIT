class GiaoVien:
    ma_gv = 1

    def __init__(self, ten, ma_xet_tuyen, diem_tin_hoc, diem_chuyen_mon):
        self.ma = "GV{:02d}".format(GiaoVien.ma_gv)
        GiaoVien.ma_gv += 1
        self.ten = ten
        self.ma_xet_tuyen = ma_xet_tuyen
        self.diem_tin_hoc = diem_tin_hoc
        self.diem_chuyen_mon = diem_chuyen_mon
        self.mon=self.Find(ma_xet_tuyen)
        
    def Find(self,ma_xet_tuyen):
        if ma_xet_tuyen[0]=='A':
            return "TOAN"
        elif ma_xet_tuyen[0]=='B':
            return "LY"
        else:
            return "HOA"

    def tinh_tong_diem(self):
        diemcong=0
        if self.ma_xet_tuyen[1]=='1':
            diemcong=2.0
        elif self.ma_xet_tuyen[1]=='2':
            diemcong=1.5
        elif self.ma_xet_tuyen[1]=='3':
            diemcong=1.0
        
        diem_tong = self.diem_tin_hoc * 2 + self.diem_chuyen_mon+diemcong
  
        return round(diem_tong, 1)

    def ket_qua(self):
        return "TRUNG TUYEN" if self.tinh_tong_diem() >= 18 else "LOAI"

def main():
    n = int(input())
    danh_sach_giao_vien = []

    for i in range(n):
        ten = input().strip()
        ma_xet_tuyen = str(input())
        diem_tin_hoc = float(input())
        diem_chuyen_mon = float(input())

        giao_vien = GiaoVien(ten, ma_xet_tuyen, diem_tin_hoc, diem_chuyen_mon)
        danh_sach_giao_vien.append(giao_vien)

    # Sắp xếp danh sách theo tổng điểm giảm dần
    danh_sach_giao_vien.sort(key=lambda gv: gv.tinh_tong_diem(), reverse=True)
    
    # In danh sách
    for gv in danh_sach_giao_vien:
        print(f"{gv.ma} {gv.ten} {gv.mon} {gv.tinh_tong_diem():.1f} {gv.ket_qua()}")

if __name__ == "__main__":
    main()

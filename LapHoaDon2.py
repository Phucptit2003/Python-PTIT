from datetime import datetime, timedelta

class KhachHang:
    ma_khach_hang = 1

    def __init__(self, ten, so_phong, ngay_nhan_phong, ngay_tra_phong, tien_dich_vu):
        self.ma = "KH{:02d}".format(KhachHang.ma_khach_hang)
        KhachHang.ma_khach_hang += 1
        self.ten = ten
        self.so_phong = so_phong
        self.ngay_nhan_phong = datetime.strptime(ngay_nhan_phong, "%d/%m/%Y")
        self.ngay_tra_phong = datetime.strptime(ngay_tra_phong, "%d/%m/%Y")
        self.tien_dich_vu = tien_dich_vu
        self.tientheotang=self.TinhTheoTang(so_phong)
        
    def TinhTheoTang(self,so_phong):
        tien=0
        if so_phong[0]=='1':
            tien=25
        elif so_phong[0]=='2':
            tien=34
        elif so_phong[0]=='3':
            tien=50
        elif so_phong[0]== '4':
            tien=80
        return tien

    def tinh_thanh_tien(self):
        so_ngay_oo = (self.ngay_tra_phong - self.ngay_nhan_phong).days+1
        thanh_tien = so_ngay_oo * self.tientheotang + self.tien_dich_vu
        return thanh_tien

def main():
    n = int(input())
    danh_sach_khach_hang = []

    for i in range(n):
        ten = input().strip()
        so_phong = str(input())
        ngay_nhan_phong = input().strip()
        ngay_tra_phong = input().strip()
        tien_dich_vu = int(input())
        khach_hang = KhachHang(ten, so_phong, ngay_nhan_phong, ngay_tra_phong, tien_dich_vu)
        danh_sach_khach_hang.append(khach_hang)

    
    # Sắp xếp danh sách theo tổng tiền giảm dần
    danh_sach_khach_hang.sort(key=lambda khach_hang: -khach_hang.tinh_thanh_tien())
    
    # In danh sách
    for i, khach_hang in enumerate(danh_sach_khach_hang):
        so_ngay_oo = (khach_hang.ngay_tra_phong - khach_hang.ngay_nhan_phong).days+1
        thanh_tien = khach_hang.tinh_thanh_tien()
        print(f"{khach_hang.ma} {khach_hang.ten} {khach_hang.so_phong} {so_ngay_oo} {round(thanh_tien)}")

if __name__ == "__main__":
    main()

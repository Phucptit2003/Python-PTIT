class HoaDon:
    def __init__(self, ma_mat_hang, ten_mat_hang, so_luong, don_gia, chiet_khau):
        self.ma_mat_hang = ma_mat_hang
        self.ten_mat_hang = ten_mat_hang
        self.so_luong = so_luong
        self.don_gia = don_gia
        self.chiet_khau = chiet_khau

    def tinh_tong_tien(self):
        return self.so_luong * self.don_gia - self.chiet_khau

def main():
    n = int(input())
    danh_sach_hoa_don = []

    for i in range(n):
        ma_mat_hang = input().strip()
        ten_mat_hang = input().strip()
        so_luong = int(input())
        don_gia = int(input())
        chiet_khau = int(input())

        hoa_don = HoaDon(ma_mat_hang, ten_mat_hang, so_luong, don_gia, chiet_khau)
        danh_sach_hoa_don.append(hoa_don)

    # Sắp xếp danh sách theo tổng tiền giảm dần
    danh_sach_hoa_don.sort(key=lambda hoa_don: hoa_don.tinh_tong_tien(), reverse=True)
    
    # In danh sách
    for hoa_don in danh_sach_hoa_don:
        tong_tien = hoa_don.tinh_tong_tien()
        print(f"{hoa_don.ma_mat_hang} {hoa_don.ten_mat_hang} {hoa_don.so_luong} {hoa_don.don_gia} {hoa_don.chiet_khau} {tong_tien}")

if __name__ == "__main__":
    main()

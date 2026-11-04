"""Câu 5a: Khai báo lớp ĐiệnThoai và phương thức hiển thị."""
class DienThoai:
    def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self):
        print("Mã máy:", self.MaMay)
        print("Tên máy:", self.TenMay)
        print("Hãng sản xuất:", self.HangSanXuat)
        print("Dung lượng pin:", self.DungLuongPin)
        print("Giá bán:", self.GiaBan)

    def du_lieu(self):
        return (self.MaMay, self.TenMay, self.HangSanXuat,
                self.DungLuongPin, self.GiaBan)

if __name__ == "__main__":
    dt = DienThoai("TEST", "May mau", "Hang mau", 4000, 1000000)
    dt.thongtindienthoai()
    print("C5A =", dt.du_lieu())

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
        return (self.MaMay, self.TenMay, self.HangSanXuat, self.DungLuongPin, self.GiaBan)

def main():
    dt1 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    dt2 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)
    dt1.thongtindienthoai()
    dt2.thongtindienthoai()
    print("C5A =", all(hasattr(DienThoai, x) for x in ("__init__", "thongtindienthoai")))
    print("C5B1 =", dt1.du_lieu())
    print("C5B2 =", dt2.du_lieu())

if __name__ == "__main__":
    main()

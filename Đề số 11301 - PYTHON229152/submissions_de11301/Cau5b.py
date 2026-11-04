"""Câu 5b: Tạo 2 đối tượng ĐiệnThoai theo đề và hiển thị."""
from Cau5a import DienThoai

if __name__ == "__main__":
    dt1 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    dt2 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)
    dt1.thongtindienthoai()
    dt2.thongtindienthoai()
    print("C5B1 =", dt1.du_lieu())
    print("C5B2 =", dt2.du_lieu())

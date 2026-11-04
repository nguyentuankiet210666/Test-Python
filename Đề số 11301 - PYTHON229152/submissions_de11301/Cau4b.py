"""Câu 4b: Xóa sách theo mã (dùng thư viện đã nhập ở câu 4a)."""
from Cau4a import nhap_thu_vien

def xoa_sach(thu_vien, ma):
    if ma in thu_vien:
        del thu_vien[ma]
        return True
    return False

if __name__ == "__main__":
    thu_vien = nhap_thu_vien()
    ma = input("Mã số sách cần xóa: ")
    da_xoa = xoa_sach(thu_vien, ma)
    if not da_xoa:
        print("Không tìm thấy cuốn sách cần xóa.")
    print("C4B_FOUND =", da_xoa)
    print("C4B =", thu_vien)

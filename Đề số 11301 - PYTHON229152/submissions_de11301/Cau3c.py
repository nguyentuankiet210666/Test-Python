"""Câu 3c: Đếm số lần xuất hiện của k trong danh sách."""
from Cau3a import nhap_danh_sach

def dem_k(ds, k):
    return ds.count(k)

if __name__ == "__main__":
    ds = nhap_danh_sach()
    k = int(input("Nhập k: "))
    print("C3C =", dem_k(ds, k))

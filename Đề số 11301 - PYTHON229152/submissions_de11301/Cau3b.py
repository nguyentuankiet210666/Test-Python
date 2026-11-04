"""Câu 3b: Tổng các số dương chẵn trong danh sách."""
from Cau3a import nhap_danh_sach

def tong_duong_chan(ds):
    return sum(x for x in ds if x > 0 and x % 2 == 0)

if __name__ == "__main__":
    ds = nhap_danh_sach()
    print("C3B =", tong_duong_chan(ds))

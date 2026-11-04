"""Câu 3a: Nhập danh sách số nguyên đến khi gặp 0."""
def nhap_danh_sach():
    ds = []
    while True:
        x = int(input("Nhập số nguyên (0 để dừng): "))
        if x == 0:
            break
        ds.append(x)
    return ds

if __name__ == "__main__":
    ds = nhap_danh_sach()
    print("C3A =", ds)

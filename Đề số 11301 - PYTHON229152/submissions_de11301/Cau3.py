def nhap_danh_sach():
    ds = []
    while True:
        x = int(input("Nhập số nguyên (0 để dừng): "))
        if x == 0:
            break
        ds.append(x)
    return ds

def main():
    ds = nhap_danh_sach()
    print("C3A =", ds)
    print("C3B =", sum(x for x in ds if x > 0 and x % 2 == 0))
    k = int(input("Nhập k: "))
    print("C3C =", ds.count(k))

if __name__ == "__main__":
    main()

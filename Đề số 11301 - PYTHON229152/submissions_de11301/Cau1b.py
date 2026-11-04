"""Câu 1b: Đếm số chữ số lẻ của số nguyên dương n."""

def dem_chu_so_le(n):
    dem = 0
    while n > 0:
        chu_so = n % 10
        if chu_so % 2 != 0:
            dem += 1
        n //= 10
    return dem

if __name__ == "__main__":
    from Cau1a import nhap_n

    n = nhap_n()
    print("C1B =", dem_chu_so_le(n))

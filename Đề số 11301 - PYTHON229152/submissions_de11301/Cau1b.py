n = int(input("Nhap n: "))
while n < 1 or n > 1500:
    n = int(input("Nhap lai n: "))

def dem_chu_so_le(n):
    dem = 0
    while n > 0:
        so = n % 10
        if so % 2 != 0:
            dem += 1
        n = n // 10
    return dem

print("C1B =", dem_chu_so_le(n))

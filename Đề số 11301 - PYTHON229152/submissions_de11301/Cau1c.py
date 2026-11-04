n = int(input("Nhap n: "))
while n < 1 or n > 1500:
    n = int(input("Nhap lai n: "))

def tinh_s(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / (2 * i)
    return s

print("C1C =", round(tinh_s(n), 6))

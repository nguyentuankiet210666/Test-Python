s = input("Nhap chuoi: ")
tong = 0
for ch in s:
    if ch.isdigit():
        tong += int(ch)
print("C2C =", tong)

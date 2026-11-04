from datetime import datetime

n = int(input("So sach: "))
while n <= 0:
    n = int(input("Nhap lai: "))

thu_vien = {}
for i in range(n):
    ma = input("Ma sach: ")
    ten = input("Ten sach: ")
    tac_gia = input("Tac gia: ")
    nxb = input("Nha xuat ban: ")
    nam = int(input("Nam xuat ban: "))
    while nam > datetime.now().year:
        nam = int(input("Nhap lai nam: "))
    thu_vien[ma] = [ten, tac_gia, nxb, nam]

ma_xoa = input("Ma sach can xoa: ")
if ma_xoa in thu_vien:
    del thu_vien[ma_xoa]
    print("C4B_FOUND =", True)
else:
    print("Khong tim thay sach")
    print("C4B_FOUND =", False)
print("C4B =", thu_vien)

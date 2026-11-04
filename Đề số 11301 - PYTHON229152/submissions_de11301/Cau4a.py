"""Câu 4a: Nhập và lưu thông tin sách trong dictionary."""
from datetime import datetime

def nhap_thu_vien():
    while True:
        n = int(input("Số lượng sách (>0): "))
        if n > 0:
            break
        print("Số lượng phải lớn hơn 0.")
    thu_vien = {}
    nam_hien_tai = datetime.now().year
    for stt in range(1, n + 1):
        print("Sách thứ", stt)
        ma = input("Mã số sách: ")
        ten = input("Tên sách: ")
        tac_gia = input("Tên tác giả: ")
        nxb = input("Nhà xuất bản: ")
        while True:
            nam = int(input("Năm xuất bản: "))
            if nam <= nam_hien_tai:
                break
            print("Năm xuất bản không hợp lệ.")
        thu_vien[ma] = [ten, tac_gia, nxb, nam]
    return thu_vien

if __name__ == "__main__":
    thu_vien = nhap_thu_vien()
    print("C4A =", thu_vien)

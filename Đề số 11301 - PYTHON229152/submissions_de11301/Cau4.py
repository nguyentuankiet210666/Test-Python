from datetime import datetime

def main():
    while True:
        n = int(input("Nhập số lượng sách (>0): "))
        if n > 0:
            break
        print("Số lượng phải > 0.")
    thu_vien = {}
    nam_hien_tai = datetime.now().year
    for i in range(n):
        print("Sách thứ", i + 1)
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
    print("C4A =", thu_vien)
    ma_xoa = input("Mã số sách cần xóa: ")
    da_xoa = ma_xoa in thu_vien
    if da_xoa:
        del thu_vien[ma_xoa]
    else:
        print("Không tìm thấy cuốn sách cần xóa.")
    print("C4B_FOUND =", da_xoa)
    print("C4B =", thu_vien)

if __name__ == "__main__":
    main()

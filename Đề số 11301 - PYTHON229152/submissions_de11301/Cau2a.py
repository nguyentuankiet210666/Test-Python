"""Câu 2a: Đếm ký tự chữ hoa trong chuỗi."""
def dem_chu_hoa(s):
    return sum(ch.isupper() for ch in s)

if __name__ == "__main__":
    s = input("Nhập chuỗi: ")
    print("C2A =", dem_chu_hoa(s))

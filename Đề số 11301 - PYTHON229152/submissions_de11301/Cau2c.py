"""Câu 2c: Tính tổng các chữ số có trong chuỗi."""
def tong_chu_so(s):
    return sum(int(ch) for ch in s if ch.isdigit())

if __name__ == "__main__":
    s = input("Nhập chuỗi: ")
    print("C2C =", tong_chu_so(s))

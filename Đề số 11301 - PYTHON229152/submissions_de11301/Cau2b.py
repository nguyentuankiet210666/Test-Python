"""Câu 2b: Kiểm tra chuỗi đối xứng."""
def doi_xung(s):
    return s == s[::-1]

if __name__ == "__main__":
    s = input("Nhập chuỗi: ")
    print("C2B =", doi_xung(s))

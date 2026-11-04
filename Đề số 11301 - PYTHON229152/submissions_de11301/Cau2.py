def xu_ly(s):
    dem_hoa = sum(ch.isupper() for ch in s)
    doi_xung = s == s[::-1]
    tong_chu_so = sum(int(ch) for ch in s if ch.isdigit())
    return dem_hoa, doi_xung, tong_chu_so

def main():
    s = input("Nhập chuỗi: ")
    dem_hoa, doi_xung, tong = xu_ly(s)
    print("C2A =", dem_hoa)
    print("C2B =", doi_xung)
    print("C2C =", tong)

if __name__ == "__main__":
    main()

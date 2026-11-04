"""Câu 1a: Nhập số nguyên n trong đoạn [1, 1500]."""

def nhap_n():
    while True:
        n = int(input("Nhập n (1..1500): "))
        if 1 <= n <= 1500:
            return n
        print("n phải nằm trong [1,1500], vui lòng nhập lại.")

if __name__ == "__main__":
    n = nhap_n()
    print("C1A =", n)

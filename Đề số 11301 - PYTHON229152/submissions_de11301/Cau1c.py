"""Câu 1c: Tính S = 1/2 + 1/4 + ... + 1/(2n)."""

def tinh_s(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / (2 * i)
    return s

if __name__ == "__main__":
    from Cau1a import nhap_n

    n = nhap_n()
    print("C1C =", round(tinh_s(n), 6))

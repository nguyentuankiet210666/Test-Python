def dem_chu_so_le(n):
    return sum(int(ch) % 2 == 1 for ch in str(n))

def tinh_s(n):
    return sum(1 / (2 * i) for i in range(1, n + 1))

def main():
    while True:
        n = int(input("Nhập n (1..1500): "))
        if 1 <= n <= 1500:
            break
        print("n phải nằm trong [1,1500], vui lòng nhập lại.")
    print("C1A =", n)
    print("C1B =", dem_chu_so_le(n))
    print("C1C =", round(tinh_s(n), 6))

if __name__ == "__main__":
    main()

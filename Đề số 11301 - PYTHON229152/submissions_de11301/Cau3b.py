ds = []
while True:
    x = int(input('Nhap so: '))
    if x == 0:
        break
    ds.append(x)
tong = 0
for x in ds:
    if x > 0 and x % 2 == 0:
        tong += x
print('C3B =', tong)

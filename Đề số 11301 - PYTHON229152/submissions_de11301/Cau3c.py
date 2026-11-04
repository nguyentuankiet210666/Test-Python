ds = []
while True:
    x = int(input('Nhap so: '))
    if x == 0:
        break
    ds.append(x)
k = int(input('Nhap k: '))
dem = 0
for x in ds:
    if x == k:
        dem += 1
print('C3C =', dem)

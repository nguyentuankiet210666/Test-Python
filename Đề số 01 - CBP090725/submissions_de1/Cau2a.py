x=int(input("Nhap so nguyen x: "))
y=int(input("Nhap so nguyen y: "))
for i in range(x,y+1):
    if i%2==0:
        tong=tong+i
print(f"{tong}")
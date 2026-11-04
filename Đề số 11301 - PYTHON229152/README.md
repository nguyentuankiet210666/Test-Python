# Đề số 11301 - Lập trình Python (229152)

Gồm 5 câu, chia thành **13 ý** (a/b/c), chấm tổng 10 điểm.
Đề gốc do người dùng cung cấp, tên file `Lập trình Python (229152)_ca7h30, 22-7.pdf`.

## Bài làm
Trong `submissions_de11301/`:
- `Cau1a.py`, `Cau1b.py`, `Cau1c.py`: kiểm tra n; đếm chữ số lẻ; tính tổng S.
- `Cau2a.py`, `Cau2b.py`, `Cau2c.py`: đếm chữ hoa; đối xứng; tổng chữ số.
- `Cau3a.py`, `Cau3b.py`, `Cau3c.py`: nhập list; tổng dương chẵn; đếm k.
- `Cau4a.py`, `Cau4b.py`: nhập dictionary sách; xóa theo mã.
- `Cau5a.py`, `Cau5b.py`: lớp DienThoai; tạo 2 đối tượng.

Các file `Cau1.py` ... `Cau5.py` cũ được giữ lại để tham khảo; **bộ chấm mới dùng từng file a/b/c**.

## Bộ chấm
- `test_de11301.py`: tập test cho từng ý.
- `autograde_de11301_v1.py`: lệnh chạy ngắn (gọi v2).
- `autograde_de11301_v2.py`: chi tiết PASS/FAIL, expected/actual, điểm từng ý theo đáp án gốc.

Tại thư mục chứa bộ chấm, chạy:

```powershell
python autograde_de11301_v2.py
```

## Thang điểm
| Câu | a | b | c | Tổng |
|---|---:|---:|---:|---:|
| 1 | 0.50 | 0.75 | 0.75 | 2.00 |
| 2 | 0.75 | 0.50 | 0.75 | 2.00 |
| 3 | 0.75 | 0.75 | 0.50 | 2.00 |
| 4 | 1.50 | 0.50 | - | 2.00 |
| 5 | 1.00 | 1.00 | - | 2.00 |

**Quy ước output:** `C2A = 2`, `C3B = 4`, v.v. để bộ chấm đọc đúng từng ý.
Các file b/c có thể import hàm ở file a ngay cùng thư mục.

Đề yêu cầu nộp **5 file .py** đặt trong folder `HOTEN_MSSV`.
Các file chia nhỏ là để học và test; khi nộp cần gộp mỗi câu thành một file.

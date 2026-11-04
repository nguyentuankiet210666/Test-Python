# Đề thi Python - Mã đề 11301

Nguồn: tài liệu **Lập trình Python (229152)_ca7h30, 22-7.pdf** do người dùng cung cấp.
Hình thức thực hành 90 phút; 5 câu, mỗi câu 2 điểm.

## Nội dung
- Câu 1: nhập n trong [1,1500], đếm chữ số lẻ, tính S = 1/2 + 1/4 + ... + 1/(2n).
- Câu 2: đếm chữ hoa, kiểm tra chuỗi đối xứng, cộng các chữ số.
- Câu 3: list số nguyên nhập đến số 0; tính tổng số dương chẵn; đếm k.
- Câu 4: dictionary lưu sách; xóa sách theo mã, thông báo nếu không tìm thấy.
- Câu 5: lớp DienThoai với 5 thuộc tính, khởi tạo và in thông tin hai đối tượng.

## Cấu trúc
- `submissions_de11301/Cau1.py` ... `Cau5.py`: 5 file bài làm đúng cấu trúc đề.
- `test_de11301.py`: input và expected cho từng trường hợp.
- `autograde_de11301_v1.py`: điểm vào chạy nhanh.
- `autograde_de11301_v2.py`: thông báo PASS/FAIL, lý do, điểm từng câu và tổng điểm.

## Cách chạy
Mở terminal tại thư mục này:

```bash
python autograde_de11301_v2.py
python submissions_de11301/Cau1.py
```

**Quy ước kiểm thử:** Đầu ra có dạng `C1A = 635` để tách dữ liệu cần chấm khỏi lời nhắc nhập.
Bộ chấm so sánh toàn bộ nhãn yêu cầu (không chỉ khớp chuỗi con).
Điểm mỗi câu được tính theo tỷ lệ test PASS trên tổng số test, tối đa 2 điểm/câu.
Có thể mở rộng test trong `test_de11301.py`.

**Lưu ý:** Đề yêu cầu folder HOTEN_MSSV chứa 5 file .py khi nộp. Bộ test/chấm và README là file hỗ trợ, không thuộc 5 file nộp.

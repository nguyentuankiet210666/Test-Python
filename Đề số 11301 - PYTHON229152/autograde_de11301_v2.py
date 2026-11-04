"""Chấm từng ý theo GIÁ TRỊ KẾT QUẢ, không bắt buộc nhãn C1A/C2B.
Bỏ lời nhắc input(), chấp nhận print(2), print("Kết quả:", 2), ...
"""
import ast
import math
import os
import re
import subprocess
import sys
from pathlib import Path
from test_de11301 import tests

ROOT = Path(__file__).resolve().parent
SUBMISSIONS = ROOT / "submissions_de11301"
WEIGHTS = {
    "Cau1a": 0.50, "Cau1b": 0.75, "Cau1c": 0.75,
    "Cau2a": 0.75, "Cau2b": 0.50, "Cau2c": 0.75,
    "Cau3a": 0.75, "Cau3b": 0.75, "Cau3c": 0.50,
    "Cau4a": 1.50, "Cau4b": 0.50,
    "Cau5a": 1.00, "Cau5b": 1.00,
}
# Chạy qua runpy để loại bỏ hoàn toàn lời nhắc input() khỏi stdout.
# Giá trị người học print() vẫn được giữ nguyên.
RUNNER = """
import builtins, runpy, sys
original_input = builtins.input
builtins.input = lambda prompt='': original_input()
runpy.run_path(sys.argv[1], run_name='__main__')
"""
NUMBER = re.compile(r"(?<![\\w.])[-+]?\\d+(?:\\.\\d+)?(?:[eE][-+]?\\d+)?(?![\\w.])")

def equal(a, b):
    if isinstance(b, float) and isinstance(a, (float, int)):
        return math.isclose(a, b, rel_tol=0, abs_tol=0.000001)
    return type(a) is type(b) and a == b

def read_value(s):
    s = s.strip()
    if not s:
        return None
    try:
        return ast.literal_eval(s)
    except (SyntaxError, ValueError):
        pass
    low = s.casefold()
    if low in ("true", "đúng", "dung", "có", "co"):
        return True
    if low in ("false", "sai", "không", "khong"):
        return False
    if "không đối xứng" in low or "khong doi xung" in low:
        return False
    if "đối xứng" in low or "doi xung" in low:
        return True
    return None

def extract(line):
    line = line.strip()
    if not line:
        return None
    # Nhận diện dữ liệu kiểu list, tuple, dict ở cuối dòng.
    for token in ("{", "[", "("):
        start = line.find(token)
        if start >= 0:
            val = read_value(line[start:])
            if isinstance(val, (dict, list, tuple)):
                return val
    # Hỗ trợ print("Tong:", 30), print("C1A: n =", 635), print(30)
    for piece in (line, line.rsplit("=", 1)[-1], line.rsplit(":", 1)[-1]):
        val = read_value(piece)
        if val is not None:
            return val
    low = line.casefold()
    if "không đối xứng" in low or "khong doi xung" in low:
        return False
    if "đối xứng" in low or "doi xung" in low:
        return True
    # Chỉ lấy số ở CUỐI dòng, không lấy các số nằm trong lời giải thích.
    # Lay gia tri cuoi dong, bat ke phan mo ta o truoc.
    last = line.split()[-1]
    return read_value(last)


def find_values(stdout):
    return [v for line in stdout.splitlines() if (v := extract(line)) is not None]

def find_phone_records(stdout):
    """Nhận 5 dòng thông tin điện thoại mà không cần in tuple."""
    lines = stdout.splitlines()
    records = []
    current = []
    field_names = ("mã máy", "tên máy", "hãng sản xuất", "dung lượng pin", "giá bán")
    for line in lines:
        if ":" not in line:
            continue
        label, value = line.split(":", 1)
        if label.strip().casefold() not in field_names:
            continue
        data = read_value(value) 
        if data is None:
            data = value.strip()
        current.append(data)
        if len(current) == 5:
            records.append(tuple(current))
            current = []
    return records

def check(name, expected_map, stdout):
    values = find_values(stdout)
    wanted = list(expected_map.values())
    # Câu 5: Có thể in mỗi thuộc tính trên một dòng, không cần in tuple.
    if name.startswith("Cau5"):
        records = [v for v in values if isinstance(v, tuple) and len(v) == 5]
        if len(records) < len(wanted):
            records = find_phone_records(stdout)
        actuals = records[-len(wanted):]
    elif name == "Cau4b":
        dictionaries = [v for v in values if isinstance(v, dict)]
        actual_dict = dictionaries[-1] if dictionaries else None
        # Trạng thái xóa được suy ra từ dictionary cuối và thông báo xóa.
        if any(isinstance(v, bool) for v in values):
            found = next(v for v in reversed(values) if isinstance(v, bool))
        elif "không tìm thấy" in stdout.casefold() or "khong tim thay" in stdout.casefold():
            found = False
        elif actual_dict == {}:
            found = True
        else:
            found = None
        actuals = [found, actual_dict]
    else:
        # Các câu còn lại mỗi file chỉ có 1 giá trị cần chấm.
        actuals = values[-1:] if values else []

    errors = []
    for i, (label, expected) in enumerate(expected_map.items()):
        actual = actuals[i] if i < len(actuals) else None
        if not equal(actual, expected):
            errors.append(f"{label}: mong đợi {expected!r}, nhận {actual!r}")
    return errors

def grade():
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    total = 0.0
    print("CHẤM BÀI - CHỈ SO SÁNH GIÁ TRỊ KẾT QUẢ")
    for name, cases in tests.items():
        maximum = WEIGHTS[name]
        path = SUBMISSIONS / (name + ".py")
        passed = 0
        print(f"\\n{'=' * 44}\\n{name} (tối đa {maximum:.2f} điểm)")
        for index, case in enumerate(cases, 1):
            if not path.exists():
                print(f"  ❌ Test {index}: thiếu file {path.name}")
                continue
            try:
                result = subprocess.run(
                    [sys.executable, "-c", RUNNER, str(path)],
                    input=case["input"], capture_output=True,
                    text=True, encoding="utf-8", errors="replace",
                    cwd=SUBMISSIONS, timeout=3, env=env
                )
                if result.returncode:
                    details = result.stderr.strip().splitlines()
                    print(f"  ❌ Test {index}: lỗi Python - {details[-1] if details else result.returncode}")
                    continue
                errors = check(name, case["expected"], result.stdout)
                if errors:
                    print(f"  ❌ Test {index}: FAIL")
                    for error in errors:
                        print("     -", error)
                    print("     Output:", repr(result.stdout.strip()[-350:]))
                else:
                    passed += 1
                    print(f"  ✅ Test {index}: PASS")
            except subprocess.TimeoutExpired:
                print(f"  ❌ Test {index}: vượt quá 3 giây")
            except OSError as error:
                print(f"  ❌ Test {index}: {error}")
        points = maximum * passed / len(cases)
        total += points
        print(f"  Kết quả: {passed}/{len(cases)} test -> {points:.2f}/{maximum:.2f} điểm")
    print(f"\\n🎯 TỔNG ĐIỂM: {total:.2f}/10.00")
    return total

if __name__ == "__main__":
    grade()

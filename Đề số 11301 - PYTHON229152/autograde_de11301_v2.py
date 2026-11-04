"""Chấm mã đề 11301: đủ nhãn, đúng giá trị, thông báo lý do FAIL."""
import ast
import math
import subprocess
import sys
from pathlib import Path
from test_de11301 import tests

ROOT = Path(__file__).resolve().parent
SUBMISSIONS = ROOT / "submissions_de11301"

def values_equal(actual, expected):
    if isinstance(expected, float) and isinstance(actual, (float, int)):
        return math.isclose(actual, expected, rel_tol=0, abs_tol=1e-6)
    return type(actual) is type(expected) and actual == expected

def parse_output(stdout):
    values = {}
    for line in stdout.splitlines():
        if " = " not in line:
            continue
        key, raw = line.split(" = ", 1)
        key = key.strip()
        try:
            values[key] = ast.literal_eval(raw.strip())
        except (SyntaxError, ValueError):
            values[key] = raw.strip()
    return values

def grade():
    total = 0.0
    for filename, cases in tests.items():
        path = SUBMISSIONS / (filename + ".py")
        passed = 0
        print(f"\n{'=' * 46}\n{filename} (tối đa 2 điểm)")
        for index, case in enumerate(cases, 1):
            if not path.is_file():
                print(f"  ❌ Test {index}: không tìm thấy file {path.name}")
                continue
            try:
                r = subprocess.run(
                    [sys.executable, str(path)],
                    input=case["input"], capture_output=True,
                    text=True, encoding="utf-8", errors="replace",
                    timeout=3, cwd=str(SUBMISSIONS)
                )
                if r.returncode != 0:
                    last_error = r.stderr.strip().splitlines()
                    reason = last_error[-1] if last_error else f"mã thoát {r.returncode}"
                    print(f"  ❌ Test {index}: lỗi chạy - {reason}")
                    continue
                actual = parse_output(r.stdout)
                mismatches = []
                for key, expected in case["expected"].items():
                    if key not in actual:
                        mismatches.append(f"{key}: thiếu kết quả")
                    elif not values_equal(actual[key], expected):
                        mismatches.append(f"{key}: mong đợi {expected!r}, nhận {actual[key]!r}")
                if mismatches:
                    print(f"  ❌ Test {index}: FAIL")
                    for reason in mismatches:
                        print("     -", reason)
                else:
                    passed += 1
                    print(f"  ✅ Test {index}: PASS")
            except subprocess.TimeoutExpired:
                print(f"  ❌ Test {index}: quá thời gian 3 giây")
            except OSError as exc:
                print(f"  ❌ Test {index}: không thể chạy - {exc}")
        score = round(2 * passed / len(cases), 2)
        total += score
        print(f"  Kết quả: {passed}/{len(cases)} test, {score:.2f}/2.00 điểm")
    print(f"\n🎯 TỔNG ĐIỂM MÃ ĐỀ 11301: {total:.2f}/10.00")
    return total

if __name__ == "__main__":
    grade()

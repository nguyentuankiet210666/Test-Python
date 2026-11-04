"""Chấm riêng 13 ý của mã đề 11301, PASS/FAIL và lý do cụ thể."""
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
# Điểm từng ý theo đáp án chính thức, tổng 10 điểm
WEIGHTS = {
    "Cau1a": 0.50, "Cau1b": 0.75, "Cau1c": 0.75,
    "Cau2a": 0.75, "Cau2b": 0.50, "Cau2c": 0.75,
    "Cau3a": 0.75, "Cau3b": 0.75, "Cau3c": 0.50,
    "Cau4a": 1.50, "Cau4b": 0.50,
    "Cau5a": 1.00, "Cau5b": 1.00,
}
LABEL = re.compile(r"(C[1-5][A-C](?:_FOUND|[12])?)\s*=\s*(.*)$")

def parse_output(stdout):
    values = {}
    for line in stdout.splitlines():
        match = LABEL.search(line)
        if not match:
            continue
        key, raw = match.groups()
        try:
            values[key] = ast.literal_eval(raw.strip())
        except (ValueError, SyntaxError):
            values[key] = raw.strip()
    return values

def equal(actual, expected):
    if isinstance(expected, float) and isinstance(actual, (int, float)):
        return math.isclose(actual, expected, abs_tol=1e-6, rel_tol=0)
    return type(actual) is type(expected) and actual == expected

def grade():
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    total = 0.0
    print("CHẤM BÀI PYTHON - MÃ ĐỀ 11301")
    for name, cases in tests.items():
        max_points = WEIGHTS[name]
        path = SUBMISSIONS / f"{name}.py"
        passed = 0
        print(f"\n{'=' * 48}\n{name} (tối đa {max_points:.2f} điểm)")
        for i, case in enumerate(cases, 1):
            if not path.is_file():
                print(f"  ❌ Test {i}: không tìm thấy {path.name}")
                continue
            try:
                result = subprocess.run(
                    [sys.executable, str(path)],
                    input=case["input"], capture_output=True,
                    text=True, encoding="utf-8", errors="replace",
                    timeout=3, cwd=SUBMISSIONS, env=env
                )
                if result.returncode:
                    lines = result.stderr.strip().splitlines()
                    reason = lines[-1] if lines else f"exit code {result.returncode}"
                    print(f"  ❌ Test {i}: lỗi chạy - {reason}")
                    continue
                actual = parse_output(result.stdout)
                issues = []
                for key, expected in case["expected"].items():
                    if key not in actual:
                        issues.append(f"{key}: thiếu kết quả")
                    elif not equal(actual[key], expected):
                        issues.append(f"{key}: mong đợi {expected!r}; thực tế {actual[key]!r}")
                if issues:
                    print(f"  ❌ Test {i}: FAIL")
                    print(f"     Input: {case['input']!r}")
                    for issue in issues:
                        print("    -", issue)
                else:
                    passed += 1
                    print(f"  ✅ Test {i}: PASS")
            except subprocess.TimeoutExpired:
                print(f"  ❌ Test {i}: quá thời gian 3 giây")
            except OSError as error:
                print(f"  ❌ Test {i}: lỗi thực thi - {error}")
        score = max_points * passed / len(cases)
        total += score
        print(f"  Kết quả: {passed}/{len(cases)} test -> {score:.2f}/{max_points:.2f} điểm")

    print(f"\n🎯 TỔNG ĐIỂM MÃ ĐỀ 11301: {total:.2f}/10.00")
    return total

if __name__ == "__main__":
    grade()

"""Test riêng từng ý a/b/c của mã đề 11301.
Mỗi test có input và expected (mọi nhãn đều phải đúng).
"""
tests = {
    "Cau1a": [
        {"input": "635\n", "expected": {"C1A": 635}},
        {"input": "0\n1501\n1\n", "expected": {"C1A": 1}},
        {"input": "1500\n", "expected": {"C1A": 1500}},
    ],
    "Cau1b": [
        {"input": "635\n", "expected": {"C1B": 2}},
        {"input": "246\n", "expected": {"C1B": 0}},
        {"input": "1111\n", "expected": {"C1B": 4}},
    ],
    "Cau1c": [
        {"input": "1\n", "expected": {"C1C": 0.5}},
        {"input": "3\n", "expected": {"C1C": 0.916667}},
        {"input": "635\n", "expected": {"C1C": 3.515814}},
    ],
    "Cau2a": [
        {"input": "AbC123\n", "expected": {"C2A": 2}},
        {"input": "abc\n", "expected": {"C2A": 0}},
        {"input": "ABC\n", "expected": {"C2A": 3}},
    ],
    "Cau2b": [
        {"input": "Ab1bA\n", "expected": {"C2B": True}},
        {"input": "abc\n", "expected": {"C2B": False}},
        {"input": "12321\n", "expected": {"C2B": True}},
    ],
    "Cau2c": [
        {"input": "AbC123\n", "expected": {"C2C": 6}},
        {"input": "hello\n", "expected": {"C2C": 0}},
        {"input": "a90b5\n", "expected": {"C2C": 14}},
    ],
    "Cau3a": [
        {"input": "1\n2\n-4\n2\n0\n", "expected": {"C3A": [1, 2, -4, 2]}},
        {"input": "0\n", "expected": {"C3A": []}},
        {"input": "3\n5\n-2\n0\n", "expected": {"C3A": [3, 5, -2]}},
    ],
    "Cau3b": [
        {"input": "1\n2\n-4\n2\n0\n", "expected": {"C3B": 4}},
        {"input": "0\n", "expected": {"C3B": 0}},
        {"input": "3\n5\n-2\n0\n", "expected": {"C3B": 0}},
    ],
    "Cau3c": [
        {"input": "1\n2\n-4\n2\n0\n2\n", "expected": {"C3C": 2}},
        {"input": "0\n5\n", "expected": {"C3C": 0}},
        {"input": "3\n5\n-2\n0\n3\n", "expected": {"C3C": 1}},
    ],
    "Cau4a": [
        {"input": "1\nS01\nPython\nAn\nNXB A\n2020\n", "expected": {"C4A": {"S01": ["Python", "An", "NXB A", 2020]}}},
        {"input": "1\nS02\nCTDL\nBinh\nNXB B\n2022\n", "expected": {"C4A": {"S02": ["CTDL", "Binh", "NXB B", 2022]}}},
    ],
    "Cau4b": [
        {"input": "1\nS01\nPython\nAn\nNXB A\n2020\nS01\n", "expected": {"C4B_FOUND": True, "C4B": {}}},
        {"input": "1\nS02\nCTDL\nBinh\nNXB B\n2022\nS99\n", "expected": {"C4B_FOUND": False, "C4B": {"S02": ["CTDL", "Binh", "NXB B", 2022]}}},
    ],
    "Cau5a": [
        {"input": "", "expected": {"C5A": ("TEST", "May mau", "Hang mau", 4000, 1000000)}},
    ],
    "Cau5b": [
        {"input": "", "expected": {"C5B1": ("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000), "C5B2": ("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)}},
    ],
}

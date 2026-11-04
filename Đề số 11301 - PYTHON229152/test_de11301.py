"""Các trường hợp kiểm thử bám theo 5 câu của mã đề 11301.
expected là ánh xạ nhãn -> giá trị Python; mỗi nhãn đều phải đúng.
"""
tests = {
    "Cau1": [
        {"input": "635\n", "expected": {"C1A": 635, "C1B": 2, "C1C": 3.515814}},
        {"input": "0\n1501\n1\n", "expected": {"C1A": 1, "C1B": 1, "C1C": 0.5}},
        {"input": "246\n", "expected": {"C1A": 246, "C1B": 0, "C1C": 3.042289}},
    ],
    "Cau2": [
        {"input": "AbC123\n", "expected": {"C2A": 2, "C2B": False, "C2C": 6}},
        {"input": "Ab1bA\n", "expected": {"C2A": 2, "C2B": True, "C2C": 1}},
        {"input": "12321\n", "expected": {"C2A": 0, "C2B": True, "C2C": 9}},
    ],
    "Cau3": [
        {"input": "1\n2\n-4\n2\n0\n2\n", "expected": {"C3A": [1, 2, -4, 2], "C3B": 4, "C3C": 2}},
        {"input": "0\n5\n", "expected": {"C3A": [], "C3B": 0, "C3C": 0}},
        {"input": "3\n5\n-2\n0\n3\n", "expected": {"C3A": [3, 5, -2], "C3B": 0, "C3C": 1}},
    ],
    "Cau4": [
        {"input": "1\nS01\nPython\nAn\nNXB A\n2020\nS01\n", "expected": {"C4A": {"S01": ["Python", "An", "NXB A", 2020]}, "C4B_FOUND": True, "C4B": {}}},
        {"input": "1\nS02\nCau truc du lieu\nBinh\nNXB B\n2022\nS99\n", "expected": {"C4A": {"S02": ["Cau truc du lieu", "Binh", "NXB B", 2022]}, "C4B_FOUND": False, "C4B": {"S02": ["Cau truc du lieu", "Binh", "NXB B", 2022]}}},
    ],
    "Cau5": [
        {"input": "", "expected": {"C5A": True, "C5B1": ("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000), "C5B2": ("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)}},
    ],
}

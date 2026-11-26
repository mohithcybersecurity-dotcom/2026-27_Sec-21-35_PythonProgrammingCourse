list_data = [
    {"name": "Anu", "marks": 75},
    {"name": "Ravi", "marks": 90},
    {"name": "Sita", "marks": 82},
]

list_by_marks = sorted(list_data, key=lambda d: d["marks"])
print("By marks ascending:", list_by_marks)

list_by_marks_desc = sorted(list_data, key=lambda d: d["marks"], reverse=True)
print("By marks descending:", list_by_marks_desc)
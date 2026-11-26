name = "Krishna"
marks = 86

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

dict_data = {"name": name, "marks": marks, "grade": grade}
print("Record:", dict_data)
for key, value in dict_data.items():
    print(f"{key}: {value}")
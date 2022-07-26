number_of_students = int(input())
students = {}
for _ in range(number_of_students):
    line = tuple(input().split())
    student, grade = line
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for key, values in students.items():
    print(f"{key} -> {' '.join(map(str, values))} (avg: {sum(values)/len(values):.2f})")

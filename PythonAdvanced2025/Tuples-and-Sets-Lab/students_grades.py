n = int(input())
students = {}

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)

    if name not in students:
        students[name] = []
    students[name].append(grade)

for names, grades in students.items():
    grades_str = " ".join(f"{g:.2f}" for g in grades)
    average = sum(grades) / len(grades)
    print(f"{names} -> {grades_str} (avg: {average:.2f})")



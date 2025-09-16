# students = {}
#
# while True:
#     student_information = input()
#
#     if ":" not in student_information:
#         break
#
#     name, student_id, course = student_information.split(":")
#
#     if course not in students:
#         students[course] = []
#     students[course].append((name, student_id))
#
# course_to_search = student_information
#
# for name, student_id in students.get(course_to_search, []):
#     print(f"{name} - {student_id}")


students = {}

while True:
    student_information = input()

    if ":" not in student_information:
        break

    name, student_id, course = student_information.split(":")

    if course not in students:
        students[course] = []
    students[course].append((name, student_id))

course_to_search = student_information

for name, student_id in students.get(course_to_search, []):
    print(f"{name} - {student_id}")



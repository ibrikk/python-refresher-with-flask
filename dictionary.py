friends = [
  {"name": "Rolf", "age": 24},
  {"name": "Adam", "age": 30},
  {"name": "Anne", "age": 27},
]

print(friends[1]["name"])

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
  print(f"{student}: {student_attendance[student]}")

for student, attendance in student_attendance.items():
  print(f"{student}: {attendance}")
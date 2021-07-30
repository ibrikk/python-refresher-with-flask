people = [("Michael", 42, "Mechanic"), ("Ibrahim", 25, "Developer"), ("Cameron", 27, "Designer")]

for name, age, profession in people:
  print(f"Name: {name}, Age: {age}, Profession: {profession}")

  person = ("Bob", 42, "Mechanic")
  name, _, profession = person
  print(name, profession)

  head, *tail = [1, 2, 3, 4, 5]
  print(head)
  print(tail)
def named(name, age):
  print(name, age)

details = {"name": "Bob", "age": 25}

named(**details)


def named1(**kwargs):
  print(**kwargs)

details = {"name": "Bob", "age": 25}

named(**details)

def named_nicely(**kwargs):
  named(**kwargs)
  for arg, value in kwargs.items():
    print(f"{arg}: {value}")

named_nicely(name="Bob", age=25)

list = ["Bob", "Rolf", "Anne"] # can manipulate
tuple = ("Bob", "Rolf", "Anne") # can't edit
set = {"Bob", "Rolf", "Anne"} # not ordered like others

print(list[0])
print(tuple[0])

list.append("Ibrahim")
print(list)

list.remove("Bob")
print(list)

set.add("Ibrahim")
print(set)

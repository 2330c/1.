guests = ["Edison", "Jefferson", "Washington"]

name = guests[0].title()
print("Welcome, " + name)

name = guests[1].title()
print("Welcome, " + name)

name = guests[-1].title()
print("Welcome, " + name)

del(guests[0])
guests.insert(0, "Adams")

name = guests[0].title()
print("Welcome, " + name)

name = name = guests[1].title()
print("Welcome, " + name)

name = guests[-1].title()
print("Welcome, " + name)

print("I found a bigger table")
guests.insert(0, "Monroe")
guests.insert(1, "Madison")
guests.append("Lincoln")

name = guests[0].title()
print(name + ", I invite you to the dinner.")

name = guests[1].title()
print(name + ", I invite you to the dinner.")

name = guests[2].title()
print(name + ", I invite you to the dinner.")

name = guests[3].title()
print(name + ", I invite you to the dinner.")

name = guests[4].title()
print(name + ", I invite you to the dinner.")

name = guests[-1].title()
print(name + ", I invite you to the dinner.")
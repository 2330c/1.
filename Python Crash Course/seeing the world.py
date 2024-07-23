locations = ['Paris', 'Italy', 'South Korea', 'Mexico', 'Canada']

print("Here is the original order:")
print(locations)

print("\nHere is the list in alphabetical order")
print(sorted(locations))

print("\nHere is the original order:")
print(locations)

print("Here is the list in reverse alphabetical order")
print(sorted(locations, reverse=True))

print("\nHere is the original order:")
print(locations)

print("\nHere is the reversed order:")
locations.reverse()
print(locations)

print("\nHere is the original order")
locations.reverse()
print(locations)

print("\nHere is the list in alphabetical order")
locations.sort()
print(locations)

print("\nHere is the list in reverse alphabetical order")
locations.sort(reverse=True)
print(locations)
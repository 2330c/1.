cubes = [x**3 for x in range(1,11)]

for y in cubes:
    print(y)

cubes2 = []

for x in range(1,11):
    cubes2.append(x**3)

print(cubes2[0])
print(cubes2[1])
#...
print(cubes2[9])

for x in range(10):
    print(cubes2[x])
line = "Row, row, row your boat"
print(line.count('row'))

print(line.lower().count('row'))

with open('newton.txt') as file_object:
    contents = file_object.read()
    contents[:100]
    contents_lower = contents.lower()
print(contents_lower.count('light'))
print(contents_lower.count('is'))
print(contents_lower.count(' is '))
print(contents_lower.count(' is.'))
print(contents_lower.count(' is,'))
print(contents_lower.count('refraction'))
print(contents_lower.count('parabola'))
print(contents_lower.count('parabolic'))
print(contents_lower.count('ellipse'))
print(contents_lower.count('circle'))
print(contents_lower.count('sphere'))
print(contents_lower.count('quadratic'))
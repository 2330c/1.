import json

numbers = input("What's your favorite number?")

filename = 'favorite_numbers'
with open('favorite_numbers', 'w') as f_obj:
    json.dump(numbers, f_obj)

print(numbers)
import json
filename = 'favorite_number'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    numbers = input("What's your favorite number? ")
    with open('favorite_number', 'w') as f_obj:
        json.dump(numbers, f_obj)
        print(numbers)
else:
    print("I know your favorite number! It's " + username)
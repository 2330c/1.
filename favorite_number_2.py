import json

username = input("What's your favorite number?")

filename = 'favorite_number'
with open('favorite_number', 'w') as f_obj:
    json.dump(username, f_obj)
    print("I know your favorite number! It's " + username)
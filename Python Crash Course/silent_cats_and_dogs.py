file_names = ["cats.txt", "dogs.txt"]

for file_name in file_names:
    print("\nFile:" + file_name)
    try:
        with open(file_name) as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        pass
    else:
        print("\nFile:" + file_name)
        print(contents)
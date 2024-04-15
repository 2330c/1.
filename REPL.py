print("Planet data program")
print("""To keep track of planets' orbital periods,
      distances from the sun, and day lengths.""")

class Planet:
    def __init__(self,name): #constructor = __init__
            self.name = name

planets = {}

def add():
    name = input("Name: ")
    if name in planets:
        print("Sorry,", name, "is already present.")
    else:
        planets[name] = Planet(name)

def delete():
    def delete():
    name = input("Name: ")
    if name in planets:
        confirm = input("Are you sure you want to delete" + name + "(yes/no): ")
        if confirm.lower() == "yes":
            del name()
            print(name + "deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print("Sorry,", name, "is not found in the list of planets.")

    pass

def show():
    #TODO: print out the names of all planets in the dictionary
    #Don't assume they'll be equal to the key (even though they are) ; (use a 'for' loop like for k in __)
    pass

def edit():
    pass

def calculate():
    pass

#TODO: improve the functions above so that the user can enter orbital periods, distances, and day lengths (convert to float())
#see "classes" in Python documentation.

cmddict = {"a":add,
          "d":delete,
          "s":show,
          "e":edit,
          "c":calculate} #create a dictionary of functions for users

cmd = "" #empty string
msg = "(A)dd, (D)el, (S)how, (E)dit (C)alc, or (Q)uit: " #put things that I think the users will want to interact with
while True:
    cmd = input(msg)
    cmd=cmd.lower()
    if len(cmd) > 0 and cmd[0] in cmddict:
        cmddict[cmd[0]]()
    elif len(cmd) > 0:
        if cmd[0] == "q":
            break
        print(cmd[0]+" is not found in list of commands.") #only checks with first letter of the command
    else:
        print("please type a command.")
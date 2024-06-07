import json

print("Planet data program")
print("""To keep track of planets' orbital periods,
      distances from the sun, and day lengths.""")

class Planet:
    def __init__(self,name): #constructor = __init__
            self.name = name
            self.period = None
            self.distance = None
            self.day = None

planets = {}

def add():
    name = input("Name: ")
    if name in planets:
        print("Sorry,", name, "is already present.")
    else:
        planets[name] = Planet(name)

def delete():
    name = input("Name: ")
    if name in planets:
        confirm = input("Are you sure you want to delete " + name + " (yes/no): ")
        if confirm.lower() == "yes":
            del planets[name]
            print(name + " deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print("Sorry,", name, "is not found in the list of planets.")


def show():
    for name in planets:
        planet = planets[name]
        print("Name:",planet.name)
        if planet.period is not None:
            print("Year:",planet.period,"secs")
        if planet.distance is not None:
            print("Distance:",planet.distance,"meters")
        if planet.day is not None:
            print("Day:",planet.day,"secs")

def edit():
    name = input("Name: ")
    if name not in planets:
        print("Sorry,", name, "is not found in the list of planets.")
        return
    info = input("(T) orbital period; (A)phelion distance; (D)ay length?")
    if len(info) < 1:
        return
    info = info.lower()[0]
    if info == 't':
        t = input("Orbital period (in seconds):")
        try:
            t = float(t)
            planets[name].period = t
        except Exception:
            print("Sorry, that's not a number.")
    elif info == 'a':
        a = input("Distance from the sun (in meters):")
        try:
            a = float(a)
            planets[name].distance = a
        except Exception:
            print("Sorry, that's not a number.")
    elif info == 'd':
        d = input("Day (in seconds):")
        try:
            d = float(d)
            planets[name].day = d
        except Exception:
            print("Sorry, that's not a number.")

def calculate():
    print("Kepler's third law: period squared is proportional to distance cubed.")
    for key in planets:
        planet = planets[key]
        period = planet.period
        distance = planet.distance
        if period is None or distance is None:
            continue
        periodsquared = period**2
        distancecubed = distance**3
        print(planet.name,"period squared over distance cubed:",periodsquared/distancecubed)

cmddict = {"a":add,
          "d":delete,
          "s":show,
          "e":edit,
          "c":calculate} #create a dictionary of functions for users

with open(cmddict, 'j') as jsonfile:
    json.dump(cmddict, jsonfile)

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
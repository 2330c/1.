import csv
import random

with open("death-rate-from-malnutrition-ghe.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    percents = {} # % death rate from malnutrition by country & year
    for row in reader:
        countryyear = (row[0], row[2])
        percentage = float(row[3])
        percents[countryyear] = percentage
    print(len(percents))

def jiggle(value, amount=30):
    newvalue = value + random.uniform(-amount, amount)
    return max(newvalue,0)

def generate_choices(value):
    wrongchoice = []
    usedchoice = set()

    if value == 0:
        wrongchoice = [
            jiggle(value + 0.5,0.1), jiggle(value + 1,0.1), jiggle(value + 1.5,0.1),
            jiggle(value - 0.5,0.1), jiggle(value - 1,0.1), jiggle(value - 1.5,0.1)]
    elif value < 0.5:
        wrongchoice = [
            jiggle(value + 0.25,0.2), jiggle(value + 0.5,0.2), jiggle(value + 0.75,0.2),
            jiggle(value - 0.25,0.2), jiggle(value - 0.5,0.2), jiggle(value - 0.75,0.2)]
    elif value < 4:
        wrongchoice = [
            jiggle(value + 2,0.3), jiggle(value + 2.5,0.3), jiggle(value + 3,0.3),
            jiggle(value - 2,0.3), jiggle(value - 2.5,0.3), jiggle(value - 3,0.3)]
    else:
        wrongchoice = [
            jiggle(value*1.5,0.3), jiggle(value*2,0.3), jiggle(value*2.5,0.3),
            jiggle(value/1.5,0.3), jiggle(value/2,0.3), jiggle(value/2.5,0.3)]
    
    random.shuffle(wrongchoice)

    while len(wrongchoice) < 3:
        newchoice = jiggle(value,0.3)
        if newchoice != value and newchoice not in usedchoice:
            wrongchoice.append(newchoice)
            usedchoice.add(newchoice)

    while len(set(wrongchoice)) < 3:
        for c in range(len(wrongchoice)):
            if wrongchoice.count(wrongchoice[i]) > 1:
                wrongchoice[i] = jiggle(value, 0.3)

    if value > 4:
        wrongchoice.append(0)
    
    return wrongchoice[:3]

num_questions = 10
score = 0

for x in range(num_questions):
    length = len(percents)
    r = random.randint(0,length-1)
    key = list(percents)[r] #a country-year pair
    value = percents[key] #the % of people with malnutrition

    letters = ["A", "B", "C", "D"]
    correctchoice = value
    wrongchoice = generate_choices(value)
    choices = [correctchoice] + wrongchoice

    li = [0,1,2,3]
    random.shuffle(li) #li will denote what index to go into in choices
    print("What was the death rate from malnutrition","in",key[0],"in",key[1],"?")
    for i in range(4):
        if li[i] == 0:  # This is the correct answer choice
            print(f"{letters[i]}: {choices[0]:.2f}%")
        else:
            print(f"{letters[i]}: ", end="")
            if isinstance(choices[li[i] - 1], float):
                print(f"{choices[li[i] - 1]:.2f}%")
            else:
                print(f"{letters[i]}: {choices[li[i]]:.2f}%")

    answer = input().upper()
    index = letters.index(answer)
    if li[index]==0:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

print(f"\nYour final score is {score} out of {num_questions}.")

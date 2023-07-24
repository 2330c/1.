from words2 import glossary

import random
import csv
import datetime

def question(mc):
    '''Asks a multiple-choice question if mc is True and write-a-word otherwise.
    Returns 1 if correct and 0 if incorrect.
    Same part of speech as the correct answer'''
    global glossary
    length = len(glossary)
    r = random.randint(0,length-1)
    key = list(glossary)[r] #a word
    value = glossary[key][0] #its definition
    if mc:
        choices = random.sample(list(glossary),4) #Four random words
        if key not in choices:
            choices[random.randint(0,3)] = key
        letters = ["A.", "B.", "C.", "D."]
        for i in range(4):
            print(letters[i],choices[i])
    guessedkey = input(value + "?")
    if guessedkey == key:
        print("Correct!")
        return 1
    else:
        print("The correct answer was: " + key)
        return 0

def quiz(mc = False):
    """Multiple choice quiz if mc is True. Write-a-word if mc is False.
    Same part of speech as the correct answer."""

    global glossary
    numq = input("Number of questions?")
    numq = int(numq)
    numcorrect = 0
    for i in range(numq):
        wascorrect = question(mc) #1 if right; 0 if wrong
        numcorrect += wascorrect
    score = numcorrect / numq * 100
    print("You got " + str(score) + "%")
    dt = datetime.datetime.now()
    dts = str(dt)
    li = dts.split()
    date = li[0]
    time = li[1]
    with open("results.csv", "a", newline = "") as results: #'a' is for append to file
        writer = csv.writer(results)
        writer.writerow([date,time,'True',str(numq),str(numcorrect),str(score)])
    return

nouns = {}
verbs = {}
adjectives = {}
adverbs = {}

for k in glossary:
    v = glossary[k]
    if v[1]=="noun":
        nouns[k]=v
    elif v[1]=="verb":
        verbs[k]=v
    elif v[1]=="adjective":
        adjectives[k]=v
    elif v[1]=="adverb":
        adverbs[k]=v
    else:
        print(k,v)
print("beginning")
print(quiz.__doc__)
print(question.__doc__)
quiz(True)
print("ending")
import random

def numberGenerator(numTrials, probability):
    numSuccesses = 0
    for t in range(numTrials):
        num = random.random()
        if num < probability:
            numSuccesses += 1
    return numSuccesses

def numberOfSuccesses():
    numTrials = input("How many trials?")
    numTrials = int(numTrials)
    probability = input("Probability of success of each?")
    if "/" in probability:
        pos = probability.find("/")
        numerator = probability[:pos]
        denominator = probability[pos+1:]
        probability = float(numerator)/float(denominator)
    else:
        probability = float(probability)
    N = 10
    for i in range(N):
        print(numberGenerator(numTrials, probability), "successes.")

#except ValueError as e:
 #   print(e)
        
numberOfSuccesses()
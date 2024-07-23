import random

def numberGenerator(numTrials, probability):
    numSuccesses = 0
    for t in range(numTrials):
        num = random.random()
        if num < probability:
            numSuccesses += 1
    return numSuccesses

def numberOfSuccesses():
    numTrials = input("How many trials? ")
    numTrials = int(numTrials)
    probability = input("Probability of success of each? ")
    if "/" in probability:
        pos = probability.find("/")
        numerator = probability[:pos]
        denominator = probability[pos+1:]
        probability = float(numerator)/float(denominator)
    else:
        probability = float(probability)
    N = 10
    numsOfSuccesses = []
    for i in range(N):
        wins = numberGenerator(numTrials, probability)
        print(wins, "successes.")
        numsOfSuccesses.append(wins)
    print("They were", numsOfSuccesses)
    
    from collections import Counter
    counter = Counter(numsOfSuccesses)
    print("counter:", counter)

    proportions = []
    for k in range(N+1):
        if k in counter:
            proportions.append(counter[k]/N)
        else:
            proportions.append(0.0)
    print(proportions)

    import matplotlib.pyplot as plt
    plt.hist(numsOfSuccesses, bins=range(N+1))
    plt.show()


#except ValueError as e:
 #   print(e)
        
numberOfSuccesses()

def numTimesEquals(targetNum, trials, list):
    """Determines the number of times targetNum shows up in trials."""

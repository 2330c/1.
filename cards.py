class Deck:
    def __init__(self, values, suits, lowhigh=True):
        """values should be supplied in order.
        lowhigh indicates whether the low value can be considered high."""
        """values and suits are lists of single-character strings"""
        self.value = values
        self.suits=suits
        self.lowhigh=lowhigh
        li=[]
        for v in values:
            for s in suits:
                li.append(v+s)
        self.cards=li

import random

class Hand:
    def __init__(self, deck, numcards=5, hand=None):
        """deck should be a Deck.
        hand can be supplied as a list of cards, or else a number of cards to deal can be supplied (by default 5), which will be dealt randomly."""
        self.deck=deck
        self.numcards=numcards
        if hand is not None:
            for card in hand:
                if card not in deck.cards:
                    raise Exception("card "+str(card)+" is not in the deck.")
                self.hand=hand
                numcards=len(hand)
        else:
            self.hand = random.sample(deck.cards,numcards)
        self.numcards=numcards
        self.values = [card[0] for card in self.hand]
        self.suits = [card[1] for card in self.hand]

def flush(hand):
    """Returns whether all cards in this hand are of the same suit."""
    if len(hand.hand) == 0:
        return True #Empty hand
    thesuit=hand.hand[0][1]
    for card in hand.hand:
        suit=card[1]
        if suit != thesuit:
            return False
    return True

from collections import Counter

def fourofakind(hand):
    counter = Counter(hand.values)
    return any([counter[key]>=4 for key in counter])
    #returns whether any value associated to a key in counter is greater than or equal to 4, for each key in counter.

def ofakind(hand, number):
    "Returns whether the hand is a 'number'-of-a-kind."
    counter = Counter(hand.values)
    return any([counter[key]>=number for key in counter])

def twopair(hand):
    counter = Counter(hand.values)
    for key in counter:
        if counter[key] >= 2:
            for otherkey in counter:
                if otherkey != key and counter[otherkey] >= 2:
                    return True
                return False
            
def twopairalt(hand):
    counter = Counter(hand.values)
    howmanypairs = sum([counter[key] >= 2 for key in counter])
    return howmanypairs >= 2

def fullhouse(hand):
    """Returns whether the hand has at least one three-of-a-kind and a distinct pair."""
    counter = Counter(hand.values)
    if any([counter[key]>=3 for key in counter]):
        if any([counter[key] == 2 for key in counter]):
            return True
    return False

def straight(hand):
    counter = Counter(hand.values)
    for key in counter:
        if counter[key] > 1:
            return False
    orders=[hand.deck.value.index(v) for v in hand.values]
    if max(orders)-min(orders)==hand.numcards-1:
        return True
    if hand.deck.lowhigh:
        tops = set(hand.deck.value[-hand.numcards+1:]) #top values
        tops.add(hand.deck.value[0])
        if set(hand.values)==tops: #If the hand consists of the top values
            return True
    return False

def isit(hand,ilk):
    """Returns whther hand is of the given ilk."""
    return ilk(hand)

values = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
suits = ['♣','♦','♥','♠',]
deck = Deck(values,suits)
hand = Hand(deck,5)

n=0
while n<10:
    hand=Hand(deck)
    if straight(hand):
        print(hand.hand)
        n += 1

def dealstats(ilk, numiters = 100, numdeals = 1000):
    """Calculates the rate at which deals are of the given ilk. Ilk should be a function that returns True or False according as the hand is of the given ilk."""
    anslist=[]
    import time
    start=time.perf_counter()
    for it in range(numiters):
        S=0
        for i in range(numdeals):
            hand=Hand(deck,5)
            if ilk(hand):
                S += 1
        #print(S/numdeals, "rate of flushes among",numdeals,"hands.")
        #0.00198 expected from theory
        anslist.append(S/numdeals)
    end=time.perf_counter()
    print("Took",end-start,"seconds.")

    from statistics import mean, stdev
    print("The mean", ilk.__name__, "rate is",mean(anslist),"with standard deviation",stdev(anslist))

    import matplotlib.pyplot as plt
    plt.hist(anslist)
    plt.show()

#dealstats(fullhouse,300,1000)
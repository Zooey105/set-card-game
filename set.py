## This imports the random module from Python's library.
## The random module uses the Mersenne Twister (https://en.wikipedia.org/wiki/Mersenne_Twister)
## "The Mersenne Twister is one of the most extensively tested random number generators in existence."

import random

## This code can be ran on all platforms that have Python installed (Mac, Linux and Windows)
## It can be ran by doing the following: 
## For Mac users: put the file on your desktop and open Terminal and type/paste the following:
"""

cd ~/Desktop
python set.py

"""
## Don't know where this alien "Terminal" is? Press command-space, type "Terminal" and press enter! 

## This code has the ability to:
##      1. Generate a set (81 cards total)
##      2. Pick 3 random cards from the 81 cards
##      3. Check if 3 cards are a set
##      4. Randomly pick 3 cards until a set is found.

## This function generates a set, but is not easily usable
## because it is a list of lists of lists of tuples. 
## This means that [ [ [ (3 cards) ] ] ] which is not very fun to write code for.
def gen_set():
    color = ['red', 'purple', 'green']
    shade = ['solid', 'clear', 'shade']
    shape = ['diamond', 'squiggle', 'oval']
    number = [1, 2, 3]
    cards = [[[[(col, sha, shp, num) for col in color] for sha in shade] for shp in shape] for num in number]
    return cards

## Given the generated set, this function will flatten the
## list of lists of lists of tuples down into one list of tuples. EG = [(cow, moo), (cat, meow), (dog, bark)]
def make_set():
    fullset = []
    for a in range(0, 3):
        for b in range(0, 3):
            for c in range(0, 3):
                for d in range(0, 3):
                    fullset += [gen_set()[a][b][c][d]]
    return fullset

## This function will take the flattened list and randomly pick three
## cards from it. When the random card is picked, it is removed from the
## flattened list so there is no chance of the same card being randomly picked.
def pick_three_cards(x):
    fullset = make_set()
    threecards = []
    for i in range(0, 3):
        card = random.choice(fullset)
        fullset.remove(card)
        threecards += [card]
    return threecards

## This function will take a list of three cards and return whether it is
## a set. The criteria for this is:
## c1 = card1 attribute(n) == card2 attribute(n) == card3 attribute(n)
## c2 = card1 attribute(n) != card2 attribute(n) and
##      card1 attribute(n) != card3 attribute(n) and
##      card2 attribute(n) != card3 attribute(n)
## If there is an interation n where both of these conditions are not met,
## the three cards do not form a set and the function will return False.
def is_set(x):
    for attribute in range(0, 4):
        all_equal = (x[0][attribute] == x[1][attribute] == x[2][attribute])
        all_diff = (x[0][attribute] != x[1][attribute] and
                    x[0][attribute] != x[2][attribute] and
                    x[1][attribute] != x[2][attribute])
        if (all_equal != True and all_diff != True): return False
    return True

## This function will take a full set and randomly select three cards from it
## until a set is found. When the set is found, it will return both the
## iterations n and the found set.
def set_probability(x):
    set_found = False
    tries = 0
    while set_found == False:
        randomcards = pick_three_cards(x)
        tries += 1
        if is_set(randomcards) == True:
            set_found = True
            print "\nA set has been found after (", tries, ") random draws.\n"
            print randomcards[0]
            print randomcards[1]
            print randomcards[2], "\n"

## This "boiler-plate code" just allows the code to run when executed through terminal/cmd.
## This code should run on all platforms using the instructions given at the start of the code.
## If you want to run any of the given functions, un-comment/comment out items with ##.
if __name__ == '__main__':
    fullset = make_set()
    set_probability(fullset)
    ## To make the full set:
    ## print make_set()
    ## To randomly select three cards:
    ## print pick_three_cards(make_set())
    ## To check if a given set is a set:
    ## print is_set([('red', 'shade', 'oval', 3), ('green', 'shade', 'oval', 3), ('purple', 'shade', 'oval', 3)])

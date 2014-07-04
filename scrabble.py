#/usr/bin/python

#imprort libs
import argparse, re, sys
from operator import itemgetter

#open scrabble offical word list and and read it into a var as a list for minipulation
f = open('sowpods.txt', 'r')
text = f.read()
data = text.lower().split()

#Store wordsearch results
result = []

#CLI argument parser. Gets user tiles information
parser = argparse.ArgumentParser(description='Scabble Cheater!!!')
parser.add_argument('letters', metavar="letters", type=str,
                    help='Enter your current letters')
args = parser.parse_args()

#stores users tiles as a list and the sorts it
userLetters = args.letters.lower()
userList = list(userLetters)
userList = sorted(userList)

#dict of letter score values for word value calculation
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

#function to make sure there are only letters inputed. Returns true if digits are found
digits = re.compile('\d')
def containsDigits(d):
    return(bool(digits.search(d)))

#makes sure only one argument is passed. also checks for numbers
if len(sys.argv) < 2 or containsDigits(userLetters) == True:
    print("Please suplly only  letters as argument")
    exit(0)
#searchs word list for any possible matches and stores matches and word scores.
def wordSearch(tiles):

    for word in data:
        tileList = []
        finalScore = 0
        if len(word) <=  len(tiles):
            for letter in tiles:
                if word.find(letter) != -1:
                    tileList.insert(word.find(letter), letter)
                    score = scores[letter]
                    finalScore += score
                    if len(tileList) == len(word):
                        tileList.sort()
                        sortedWord = list(word)
                        sortedWord.sort()
                        if tileList == sortedWord:
                            result.append((word, finalScore))

    #sorts list by word score.
    sortedResults = sorted(result, key=itemgetter(1))
    for results in sortedResults:
        print(results)

wordSearch(userList)

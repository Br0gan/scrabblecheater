#/usr/bin/python

import argparse, re, sys

f = open('sowpods.txt', 'r')
text = f.read()
data = text.lower().split()

parser = argparse.ArgumentParser(description='Scabble Cheater!!!')
parser.add_argument('letters', metavar="letters", type=str,
                    help='Enter your current letters')
args = parser.parse_args()

userLetters = args.letters.lower()
userList = list(userLetters)
userList = sorted(userList)

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}


digits = re.compile('\d')
letCheck = re.compile('\w')

def containsDigits(d):
    return(bool(digits.search(d)))

if len(sys.argv) < 2 or containsDigits(userLetters) == True:
    print("Please suplly only  letters as argument")
    exit(0)

def wordSearch(l):
    for word in data:
        wl = []
        if len(word) <=  len(l):
            for letter in l:
                if word.find(letter) != -1:
                    wl.insert(word.find(letter), letter)
                    if len(wl) == len(word):
                        newWord = ''.join(wl)
                        print(newWord)
                        if newWord == word:
                            print(word)
                            result.append(word)

result = []
wordSearch(userList)
print(result)

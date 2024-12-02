import random

wordLength = int(input("How many letter are in your word?"))


letters = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]
 
word = ""

while wordLength>0:
    word = word + random.choice(letters)
    wordLength = wordLength - 1

print(word)
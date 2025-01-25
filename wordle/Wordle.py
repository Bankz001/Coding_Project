import os
import random

def wordlist():
    path = './wordle/valid-wordle-words.txt'
    if os.path.exists(path):
        with open(path, 'r') as f:
            word = f.read()
            print(random.choice(word))
            
        print(f"File not found: {path}")

wordlist()


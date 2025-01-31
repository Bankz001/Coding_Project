import os
import random
from colorama import init
from termcolor import colored

init()

def txt_to_wordlist(file_path):
    try:
        # Open the file
        with open(file_path, 'r') as file:
            # Read the content of the file
            content = file.read()           
            # Split the content into words (split by whitespace)
            word_list = content.split()    
        return word_list
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def answering(word):
    ans = input("Enter a 5 letters word : ")
    answer = ans.lower()
    while len(answer) != 5:
        print("Invalid answer")
        answer = input("Enter a 5 letters word : ")
    print('-',end='')
    answer_l = list(answer)
    word_l = list(word)
    for i in range(len(answer_l)):
        c1 = False
        c2 = False
        for j in range(len(word_l)):
            if answer_l[i] == word_l[j]:
                c1 = True
                if i==j :
                    c2 = True
        if c1 == True and c2 == True:
            print(colored(answer_l[i],'green'),end='')    
        elif c1 == True and c2 == False:
            print(colored(answer_l[i],'yellow'),end='')  
        else:
            print(colored(answer_l[i],'red'),end='')
    print()
    return answer    

file_path = './wordle/valid-wordle-words.txt'  # Replace with your file path
word_list = txt_to_wordlist(file_path)
word = random.choice(word_list)

print(word)
print("WORDLE")
print("You have 5 chances to answer the correct answer")

i = 5
answer = answering(word)
while answer != word and i>1:
    i-=1
    if answer != word :
        print("You have", i,"chances left.")
    answer = answering(word)  
    
if answer == word :
    print(colored("Congratuation",'green'))
else:
    print("The correct answer is:", word)
    
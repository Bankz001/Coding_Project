import os
import random
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

def answering():
    answer = input("Enter a 5 letters word : ")
    while len(answer) != 5:
        print("Invalid answer")
        answer = input("Enter a 5 letters word : ")
    return answer    

file_path = './wordle/valid-wordle-words.txt'  # Replace with your file path
word_list = txt_to_wordlist(file_path)
word = random.choice(word_list)

print(word)
print("WORDLE")
print("You have 5 chances to answer the correct answer")

i = 5
answer = answering()
while answer != word and i>1:
    i-=1
    if answer != word :
        print("You have", i,"chances left.")
    answer = answering()  
    
if answer == word :
    print("Congratuation")
else:
    print("The correct answer is:", word)
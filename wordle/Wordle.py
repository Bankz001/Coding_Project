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

# Example usage
file_path = './wordle/valid-wordle-words.txt'  # Replace with your file path
word_list = txt_to_wordlist(file_path)

word = random.choice(word_list)
answer = input("Enter a 5 letters word : ")

if answer == word :
    print("correct")
else : 
    print("not correct")

print(word)
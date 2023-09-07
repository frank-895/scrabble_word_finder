## THIS PROGRAM FINDS POSSIBLE SCRABBLE WORDS THAT CAN BE PLAYED WITH A SET OF LETTERS.
# Francis Snelling 06/09/2023

# define variables
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "?"]
letter_values ={"a":1, "b":3, "c":3, "d":2, "e":1, "f":4, "g":2, "h":4, "i":1, "j":8, "k":5, "l":1, "m":3, "n":1, "o":1, "p":3, "q":10, "r":1, "s":1, "t":1, "u":1, "v":4, "w":4, "x":8, "y":4, "z":10}
user_letters = []
possible_words = []
word_values = {}

# FUNCTION continually prompts until valid letter input
def prompt_letter():
    letter = ""
    while letter.lower() not in letters:
        letter = input("Enter a scrabble letter(? for blank tile): ")
    return letter.lower()

# FUNCTION returns word as string if possible otherwise returns False
def word_possible(word, user_letters):
    no_qu_marks = 0
    for letter in user_letters: # tally up number of question marks
        if letter == "?":
            no_qu_marks += 1
    counter = 0 # to count number of letters in word not possessed by user
    index = 0 # to track index of letter not possessed by user
    for letter in word:
        if letter in user_letters:
            user_letters.remove(letter) # remove from list, so double letters don't yeild error
        else:
            counter += 1
            word = word[:index] + word[index].upper() + word[index + 1:]
        if counter > no_qu_marks + 1:
            return False
        index += 1
    return word
    
# gather user information
print("This program finds the possible scrabble words that can be played with your letters.\n")
number_letters = 0
valid_numbers = ["1", "2", "3", "4", "5", "6", "7"]
while number_letters not in valid_numbers:
    number_letters = input("Enter the number of letters you have: ")
number_letters = int(number_letters)

for i in range(number_letters):
    user_letters.append(prompt_letter())

# load in valid words
valid_words = open("valid_words.txt", 'r').readlines()
for i in range(len(valid_words)):
    valid_words[i] = valid_words[i].strip().lower()

# load valid words into possible_words
for word in valid_words:
    user_letters_copy = user_letters.copy()
    return_value = word_possible(word, user_letters_copy)
    if return_value != False:
        possible_words.append(return_value)

# make dictionary of possible words and corresponding value
for word in possible_words:
    word_value = 0
    for letter in word:
        word_value += letter_values[letter.lower()]
    word_values[word] = word_value

# sort dictionary
word_values = sorted(word_values.items(), key = lambda x:x[1], reverse = True)

# display to user
current_word_value = word_values[0][1]
index = 0
print("\nThe words you can play are:")
for i in range(current_word_value):
    if word_values[index][1] == current_word_value:
        print("\nWith a value of " + str(current_word_value) + " points:")
    while word_values[index][1] == current_word_value:
        if word_values[index + 1][1] == current_word_value: # last value has no comma
            print(word_values[index][0] + ", ", end="")
        else:
            print(word_values[index][0])
        index += 1
    current_word_value = current_word_value - 1
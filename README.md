# Scrabble Word Finder

This program helps Scrabble players find possible words that can be played using a given set of letters. It takes the letters from the user and checks them against a predefined list of valid Scrabble words, calculating the Scrabble score for each possible word. The results are then displayed in descending order of point value.

## Features

- User Input: The user provides the letters they have (including wildcard tiles as ?).
- Word Matching: The program checks the given letters against a list of valid Scrabble words.
- Score Calculation: It calculates the Scrabble point value of each valid word based on Scrabble letter values.
- Results: The words and their corresponding point values are displayed, sorted by highest to lowest value.

## How It Works

- The user enters the number of letters they have (1-7), and then the letters themselves.
- The program loads a list of valid Scrabble words from a file called valid_words.txt.
- It checks if the words can be formed using the user's letters (wildcard ? tiles can be substituted for missing letters).
- The program calculates the score for each possible word and displays the results in order of their point value.

## Installation

- Clone or download this repository.
- Ensure you have a valid_words.txt file that contains valid Scrabble words, with one word per line.
- Run the program using Python

*Example*

This program finds the possible scrabble words that can be played with your letters.

```
Enter the number of letters you have: 5
Enter a scrabble letter(? for blank tile): a
Enter a scrabble letter(? for blank tile): r
Enter a scrabble letter(? for blank tile): t
Enter a scrabble letter(? for blank tile): p
Enter a scrabble letter(? for blank tile): e

The words you can play are:

With a value of 8 points:
part, taper, pater...
```

## File Structure

- scrabble_word_finder.py: The Python script containing the logic to find and score possible Scrabble words.
- valid_words.txt: A text file containing a list of valid Scrabble words, with each word on a new line.

## Lessons Learned

This project is a beginner-level Python application. Through building this project, I learned the following:

- User Input Validation: Continually prompting the user until valid input is received.
- String and List Manipulation: Handling letters, words, and lists to create meaningful output.
- Dictionary Usage: Mapping letters to point values and associating words with their corresponding scores.
- File Handling: Reading words from a text file and processing them within the program.
- Basic Sorting and Display: Sorting word-score pairs and printing them in a formatted way.

## Potential Improvements
- Add a graphical user interface (GUI) to make the program more user-friendly.
- Implement the ability to take double/triple letter or word scores into account.
- Expand the project to suggest optimal word placements on an actual Scrabble board.

**Limitations**
- The program currently only checks for words using a simple text-based approach and does not account for board layout.
- It works with a basic Scrabble word list and does not have built-in support for official Scrabble dictionaries.

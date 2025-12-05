# ''''''•  Task: Unique Word Lister 
# •	Description: Write a program that takes a sentence from the user, splits it into words, and displays only the unique words in alphabetical order.
# •	Requirements: 
# o	Prompt the user for a sentence.
# o	Split the sentence into words, ignoring case and punctuation.
# o	Use a set to store unique words.
# o	Sort the unique words alphabetically and display them.
# o	Write a function to process the sentence and return the unique words.
# o	Handle empty input gracefully.''''''
# '''

import string

def unique_words(sentence):
    # remove punctuation
    for p in string.punctuation:
        sentence = sentence.replace(p, "")

    words = sentence.lower().split()

    uniq = set(words)
    uniq = sorted(uniq)
    return uniq


sentence = input("Enter a sentence: ")

if sentence.strip() == "":
    print("Empty input, no words")
else:
    result = unique_words(sentence)
    print("Unique words:")
    for w in result:
        print(w)
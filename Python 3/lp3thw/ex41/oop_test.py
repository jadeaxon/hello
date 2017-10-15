#!/usr/bin/env python3

import random
from urllib.request import urlopen

import sys

# Source of random words.
WORD_URL = "http://learncodethehardway.org/words.txt"
# The random words.
WORDS = []

# The phrase for each code snippet.
PHRASES = {
    "class %%%(%%%):": "Make a class named %%% that is a %%%.",
    "class %%%(object):\n\tdef__init__(self, ***)": "class %%% has a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)": "class %%% has a function *** that takes self and @@@ params.",
    "*** = %%%()": "Set *** to an instance of class %%%.", "***.***(@@@)": "From ***, get the *** function and call it with args self, @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'."
}

# Do they want to drill phrases first?

if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# Load up the words from the website.
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

## print(WORDS)

# Generates concrete questions and answers by substituting random words for placeholders in the
# code snippet and English description phrase.
def convert(snippet, phrase):
    ## print(f"snippet: {snippet}")
    ## print(f"phrase: {phrase}")

    # Take a random sample of words from WORDS equal to number of %%% placeholders in the snippet.
    # Capitalize these class names.  This is all done with a list comprehension.
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    ## print(f"class_names: {class_names}") 
    other_names = random.sample(WORDS, snippet.count("***"))
    ## print(f"other_names: {other_names}")
    results = []
    param_names = []

    # Generate one or two parameter names.
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
        ## print(f"param_names: {param_names}")
    # Replace the place holders in the code snippet and English description with the randomly
    # selected words.
    for sentence in snippet, phrase:
        result = sentence[:] # Copy the list.
        # Fake class names.
        for word in class_names:
            result = result.replace("%%%", word, 1)
        # Fake other names.
        for word in other_names:
            result = result.replace("***", word, 1)
        # Fake parameter lists.
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
    ## print(f"results: {results}")
    return results

# Keep going until ^D hit.
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
        for snippet in snippets:
            ## print(snippet)
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            print(question)
            input("< ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye!")



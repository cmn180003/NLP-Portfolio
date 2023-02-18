# Homework 2
# Crystal Ngo

import sys
import pathlib
import nltk
from nltk import word_tokenize
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import itertools
from collections import Counter
from itertools import islice
from random import seed
from random import randint

seed(1234)  # Makes random number reproducible


def preprocess(rawtxt):
    '''
    Preprocesses input for usage in guessing game
    Args:
        rawtxt: a string containing all text to be processed
    Returns: list, list
        lowercase, alphabetical tokens
        lemmas that are nouns with a length > 5 and are not stopwords
    Example:
        >>>preprocess("I teach at the University of Texas at Dallas.")
        >>>['i', 'teach', 'at', 'the', 'university', 'of', 'texas', 'at', 'dallas']
        >>>['dallas']
    '''
    # Reduces tokens to lowercase alpha-only
    txt = re.sub(r'[.?!,:;()\-\n\d]', ' ', rawtxt.lower())
    ogtokens = word_tokenize(txt)

    # Removes stopwords
    stpwrds = set(stopwords.words('english'))
    tokens = [t for t in ogtokens if not t in stpwrds]

    # Only keeps words > 5 characters long
    tokens = [t for t in tokens if len(t) > 5]

    # Lemmatizes tokens and removes duplicates
    wnl = WordNetLemmatizer()
    tokens = [wnl.lemmatize(t) for t in tokens]
    tokenset = set(tokens)

    # POS tagging and prints first 20 tagged
    tags = nltk.pos_tag(tokenset)
    for i, val in enumerate(itertools.islice(tags, 20)):
        print(tags[i])

    # Creates a list of lemmas that are nouns
    nouns = [token for token, pos in tags if pos.startswith('N')]

    # Prints number of tokens and nouns
    print("Number of tokens = ")
    print(len(ogtokens))
    print("Number of nouns = ")
    print(len(nouns))

    return ogtokens, nouns


def game(wordbank):
    '''
    Runs a guessing game
    Args:
        wordbank: a list of words to be chosen at random
    Returns: N/A
    Example:
        >>>game(['heart', 'bear', 'fever'])
        >>> Points: 5
            Previous incorrect guess:
            ____
            Guess a letter:
    '''
    # Explains rules to the user
    print('Hello! This is a game similar to hangman.')
    print('You will be given 5 points to start with and a word to guess. Each wrong guess will deduct 1 point.')
    print('Each correct guess will increase your points by 1. When your point total dips below 0, you will lose.')
    print('To give up, guess "!". Guessing the whole word correctly will result in victory and award bonus points ')
    print('based on how many letters are remaining. Guess the word correctly to win!')

    replay = 'y'                                # Choice to replay game or not
    while replay =='y':
        # Sets initial score and word to guess
        ptstotal = 5                            # User score
        bonus = 0                               # Bonus for guessing early
        wrongguesses = ''                       # List of user's incorrect guesses
        answer = wordbank[randint(0, 49)][0]    # Random word user must guess

        # Generates blanks and calculates possible bonus points
        secretword = ""                         # Word as user sees it
        for i in range(len(answer)):
            secretword = "".join([secretword, '_'])
            bonus += 1

        # User guesses letters and guesses word updates
        guess = ''                                          # User guess
        while ptstotal >= 0 and guess != '!':
            print('\nPoints: ', ptstotal)                   # Prints current points
            print('Previous guesses: ' + wrongguesses)      # Prints previous wrong guesses
            print(secretword)                               # Prints hidden word with guessed letter
            guess = input("Guess a letter: ")               # Gets user's guess

            # User gives up
            if guess == '!':
                break       # Ends current game

            # User guessed whole word correctly
            if guess == answer:
                print('Great job! The word was indeed ' + answer)   # Prints confirmation message
                ptstotal += bonus               # Adds bonus to total
                print('Points: ', ptstotal)     # Prints points
                print("\n~You win!~")           # Prints congratulatory message
                break                           # Ends current game

            # User guessed a correct letter
            if answer.rfind(guess) != -1:
                print('Right!')     # Prints confirmation message
                ptstotal += 1       # Increments points
                bonus -= 1          # Decrements possible bonus

                # Updates secret word with correct guess
                for i in range(len(answer)):
                    if guess == answer[i]:
                        secretword = secretword[:i] + guess + secretword[i + 1:]

                # User completed the word
                if secretword == answer:
                    print('\nPoints: ', ptstotal)   # Prints points
                    print(secretword)               # Prints word
                    print("\n~You win!~")           # Prints congratulatory message
                    break                           # Ends current game

            # User guess wrong letter
            else:
                print('Sorry, guess again')     # Prints feedback
                ptstotal -= 1                   # Decrements points

                # Updates list of previous wrong guesses
                if wrongguesses == '':
                    wrongguesses = guess
                    continue
                wrongguesses = ', '.join([wrongguesses, guess])

        # User lost
        if ptstotal < 0:
            print('\nPoints: ', ptstotal)   # Prints points
            print('You lost!')              # Prints lose message
            print('The answer was ' + answer)   # Prints answer

        # User gave up
        if guess == '!':
            print('You gave up. The answer was: ' + answer) # Prints surrender message

        # Asks the user if they want to play again
        replay = input("Play again? y/n\n")
        if replay == 'y':
            continue
        else:
            return 0


if __name__ == '__main__':
    # Reads system argument
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
        quit()

    # Reads data
    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r') as f:
        rawtext = f.read()

    # Tokenizes raw text
    toks = word_tokenize(rawtext)
    # Makes the tokens lowercase
    toks = [t.lower() for t in toks]
    # Puts tokens in a set (no duplicates)
    uniquetok = set(toks)
    # Calculates lexical diversity
    print("Lexical diversity: %.2f" % (len(uniquetok)/len(toks)))

    # Preprocesses text and gets a list of tokens and nouns
    tokens, nouns = preprocess(rawtext)

    # Makes a dictionary for tokens with their counts
    tokendict = Counter(tokens)

    # Combines nouns and their counts in a dictionary
    dictionary = {}
    for x in nouns:
        for k, v in tokendict.items():
            if k == x:
                dictionary[k] = v

    # Sorts dictionary by most counts
    sorteddict = {}
    skeys = sorted(dictionary, key = dictionary.get, reverse = True)
    for w in skeys:
        sorteddict[w] = dictionary[w]

    #Makes and displays a list of the 50 most common words and their counts
    wordbank = list(islice(sorteddict.items(), 50))
    print(wordbank)

    # Starts game
    game(wordbank)



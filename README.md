# NLP-Portfolio
Code, code narratives, reports, and presentations produced as I learn about NLP

## Overview of NLP
Overview of NLP including terms, applications, approaches, and my interest in it. [Find it here.](Overview_of_NLP.pdf)

## Text Processing
- Program that processes employee data to be displayed in a certain manner.
- To run this program, give it the relative path to the csv file holding the data. Respond to any prompts to correct data as indicated.
- In my opinion, Python has some convenient text processing features like *capitalize()* which doesn't require the programmer to check how the string is already capitalized; it just spits out the string in a certain format. The disadvantage to these kinds of features is that they lack flexibility. For instance, if I wanted to convert a string into camel case, I would need to use a lot more creativity.
- This was my first Python program so I learned a lot. I found a common way to start a Python program with a system argument, I gained experience in making classes and functions, and I learned how to create and use pickle files. I also got a review in how to use a regex and they seem more approachable than I remembered since the regexes used here were fairly basic and I had a guide in front of me.
- [Find the code here](1_Text_Processing.py)

## Word Guessing Game
- Program that plays a word guessing game similar to hangman to the user.
- To run this program, give it the relative path to the txt file holding the raw text containing the words you want in the game. For example, you could use the first chapter of a textbook. The program will prompt the user to guess what the word is letter by letter. Below are the instructions given to the user after the text has been processed and the game is beginning:
> Hello! This is a game similar to hangman. You will be given 5 points to start with and a word to guess. Each wrong guess will deduct 1 point. Each correct guess will increase your points by 1. When your point total dips below 0, you will lose. To give up, guess "!". Guessing the whole word correctly will result in victory and award bonus points based on how many letters are remaining. Guess the word correctly to win!
- [Find the code here](2_Word_Guessing_Game.py)

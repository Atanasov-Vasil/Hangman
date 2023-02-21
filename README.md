# Hangman
Simple console game of Hangman

Hangman (https://en.wikipedia.org/wiki/Hangman_(game)) is popular game of guessing letters and wods.

In this case, it's computer vs player - computer chooses the word randomly from nearly 10000 most popular English words and the player has to guess it.

Player chooses the difficulty, which depends only on the number of attepmts that he or she gas to guess the word. Easy = 10 attempts, Medium = 8 attempts and Hard is 6 attempts.

After that player enters a letter. There are several outcomes there:
1. The player enters not a letter. The game demands a letter. It is not counted as a mistake.
2. The player enters a letter that he or she has already entered. The game demands a new letter. Again, it is not counted as a mistake.
3. The player enters a "valid" letter:
a. If it is in the word, it is a hit. The game returns how many letters in the word the player has "opened" with the current letter and prints the current status of the word
b. It is not in the word. It is counted as a mistake.
  If attempts - mistakes reaches 0, the player is pronounced "Dead" and the word is revealed.
  If attempts are still more than mistakes, the player is informed how many more attempts he or she has, and the current status of the word is printed.
If the player opens all the letters, he or she is congratulated.

After the game is finished, no matter with win or lose, there's an option for the player to play again ffor the beginning, including to choose the difficulty level. If he or she decides not to play, statistics for wins vs loses is printed.

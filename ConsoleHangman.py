import sys
import random


def correct(guess):
    if guess in word:
        if guess not in guessed:
            print("Correct!\n")
            return True
    else:
        if guess not in word and len(guess) == 1 and guess in 'abcdefghijklmnopqrstuvwxyz':
            if guess not in guessed:
                print("Incorrect!")
                return False


word_file = sys.argv[1]
word_list = open(word_file)
words = word_list.readlines()
word_list.close()

num_words = len(words)
wordArray = []
for i in range(num_words):
    wordArray.append(words[i].rstrip())

while True:
    x = random.randrange(0, 3999)
    word = wordArray[x]
    if len(word) >= 4:
        break

trys = 8
guessed = []
wrong_guesses = []

print("Welcome to Console Hangman!\n")

guessed_letters = len(word) * ['_']
print(' '.join(guessed_letters))
while trys > 0:
    print('Your bad guesses so far:', ','.join(wrong_guesses))
    guess = str(input("Guess a letter:"))
    if guess not in 'abcdefghijklmnopqrstuvwxyz':
        print("That is not a letter, try again.")
    if guess in guessed:
        print("You have already guessed that letter, try again.")
        continue
    result = correct(guess)
    guessed.append(guess)
    if result == True:
        for position, letter in enumerate(word):
            if letter == guess:
                guessed_letters[position] = letter
        print(' '.join(guessed_letters))
    else:
        trys = trys - 1
        print("You have", trys, "guesses left.\n")
        print(' '.join(guessed_letters))
        wrong_guesses.append(guess)
    if trys == 0:
        print('\nYOU LOSE')
        print('The secret word was:', word)
        quit()
    if set(word) == set(guessed_letters):
        print('\nYOU WON!')
        print('The secret word was:', word)
        quit()

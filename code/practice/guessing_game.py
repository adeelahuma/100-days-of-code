"""

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

    Keep the game going until the user types "exit"
    Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random as rd


def main():

    guess_count = 0
    guess = input('Guess a number between between 1 and 9 (including 1 and 9) or enter exit to end game: ')
    num = rd.randint(1, 10)

    while True:

        if guess == "exit":
            break

        guess_count = guess_count + 1

        if num < int(guess):
            guess = input('You guessed a larger number. Please guess a number again: ')
        elif num > int(guess):
            guess = input('You guessed a smaller number. Please guess a number again: ')
        else:
            print('You guessed correct number!')
            break

    print ('you made {} guesses'.format(guess_count))


if __name__ == "__main__":
    main()
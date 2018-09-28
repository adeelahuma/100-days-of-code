"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""


def main():

    number = int(input('Please enter a number: '))

    if number % 2 == 0 and number % 4 == 0:
        print('You have entered an even number that is multiple of 4')
    elif number % 2 == 0:
        print('You have entered an even number')
    else:
        print('You have entered an odd number')

    num = int(input('Enter a number to check: '))
    check = int(input('Enter a number to divide: '))

    if num % check == 0:
        print('check divides evenly into num')
    else:
        print('check does not divides evenly into num')


if __name__ == '__main__':
    main()
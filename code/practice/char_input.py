'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
Extras:

1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

'''

from datetime import date

def main():

    name = input("Give me your name:  ")
    age = input("Enter your age: ")

    to_be_100 = 100 - int(age)
    today_year = date.today().year

    year_100 = today_year+to_be_100

    msg = "{} you'll be 100 years old in {}.".format(name, year_100)
    print(msg)

    num = input('Enter a number: ')
    rep_msg = msg * int(num)
    print(rep_msg)

    for x in rep_msg.split('.'):
        print(x)


if __name__ == "__main__":
    main()
"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don't know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

"""


def main():
    num = int(input('Enter a number: '))

    rstart = 1
    rend = 101
    numbers = range(rstart, rend)

    divisors = [x for x in numbers if x%num == 0]
    print 'Divisors of {} between {} and {} :'.format(num, rstart, rend), divisors


if __name__ == "__main__":
    main()
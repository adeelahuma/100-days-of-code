"""
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.

"""


def get_input(default_prompt="Enter a number: "):
    return input(default_prompt)


def is_prime():
    num = int(get_input())
    count = 0
    if num == 1 or num == 2:
        print('{} is a prime number!'.format(num))
    else:
        for n in range(2, num+1):
            if num % n == 0:
                count = count + 1

            if count > 1:
                print('{} is not a prime number!'.format(num))
                break

        if count <= 1:
            print('{} is a prime number!'.format(num))


if __name__ == "__main__":
    is_prime()
"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this
2. Write this in one line of Python (don't worry if you can't figure this out at this point - we'll get to it soon)

"""
import random as rd


def main():
    # generate random lists
    a = rd.sample(range(1, 10), 8)
    b = rd.sample(range(1, 10), 5)

    common_elements = [num for num in a if num in b]

    # this could be solved as below as well using intersection between two sets
    # common_elements = set(a) & set(b)

    # there can be duplicates so convert list to set to remove duplicates
    common_elements = set(common_elements)
    print 'common elements in \n{} and {} are :\n {}'.format(a, b, common_elements)


if __name__ == "__main__":
    main()
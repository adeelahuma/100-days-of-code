"""

Let's say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

"""
import random


def list_comp():

    a = random.sample(range(0,15), 15)  # a random list
    b = [x for x in a if x%2 ==0]

    print 'a:', a
    print 'b:', b


if __name__ == "__main__":
    list_comp()
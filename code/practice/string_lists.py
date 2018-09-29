"""

Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)

"""


def main():

    # convert the word to lower case
    word = input('Enter a string: ').lower()

    # following is one way to solve this problem

    # # reverse the word
    # word_b = word[::-1]
    # is_palindrome = True
    #
    # for i in range(0, len(word)):
    #     if word[i] != word_b[i]:
    #         is_palindrome = False
    #         break
    #
    # print ('{} is {}a palindrome'.format(word, '' if is_palindrome else 'not '))

    # Another smarter way to solve the same problem is as following:
    is_palindrome = word[::] == word[::-1]
    print ('{} is {}a palindrome'.format(word, '' if is_palindrome else 'not '))


if __name__ == "__main__":
    main()
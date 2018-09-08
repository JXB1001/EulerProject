# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#

import timeit

def findAnswer():
    """ Returns the sum of all the multiples of 3 or 5 under input 1000 """
    n = 1000
    s = 0 

    for i in range(n):
        if i%3 == 0:
            s += i
        elif i%5 == 0:
            s += i

    return s


def main():
    """ Main Function """

    # finding the answer
    answer = findAnswer()
    # testing the speed of the methods
    t = timeit.timeit(findAnswer, number=1000)

    print("Answer = " + str(answer))
    print("\nTime taken to do function 1000 times")
    print("\tMethod 1: " + str(t))


if __name__ == "__main__":
    main()

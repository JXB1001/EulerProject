# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Answer = 233168

import timeit

def method1():
    """ 
        Method 1 loops through all the numbers under 1000 and
        adds them to the total if they are a mulitple of 3 or 5 
    """
    n = 1000
    s = 0 

    for i in range(n):
        if i%3 == 0:
            s += i
        elif i%5 == 0:
            s += i

    return s

def method2():
    """ Adds 3 and 5 to a total to find all the multiples under 1000 """
    n = 1000
    s = 0
    multiples = [3,5]
    total = []

    for m in multiples:
        total.append(0)

    minValue = 0
    while(minValue < 1000):
        minValue = 1000
        minPosition = 0
        for i, v in enumerate(total):
            if v < minValue:
                minValue = v
                minPosition = i

        temp = total[minPosition] + multiples[minPosition]

        if(temp < 1000) and (temp not in total):
            s += temp

        total[minPosition] = temp

    return s


def main():
    """ Main Function """

    # finding the answer
    answer1 = method1()
    answer2 = method2()

    # testing the speed of the methods
    t1 = timeit.timeit(method1, number=100)
    t2 = timeit.timeit(method2, number=100)

    print("Answer = " + str(answer1))
    print("\nTime taken to do function 100 times")
    print("\tMethod 1: " + str(t1))
    print("\tMethod 2: " + str(t2))


if __name__ == "__main__":
    main()

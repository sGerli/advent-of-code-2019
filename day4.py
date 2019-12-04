import sys
from random import randrange

def challenge1():
    """
    Create intcode processor and process input with 1202 initialization code.
    """
    startRange = 147981
    endRange = 691423
    count = 0
    for number in range(endRange - startRange):
        number += startRange
        # Check conditions
        adjacentSame = False
        decreaseing = False
        for i in range(5):
            lastNumber = number % 10
            number //= 10
            #print(number, ' ', lastNumber)
            if lastNumber == number % 10:
                adjacentSame = True
            elif lastNumber < number % 10:
                decreaseing = True
                break
        if adjacentSame and not decreaseing:
            count += 1

    print(count)

def challenge2():
    """
    Create intcode processor and process input with 1202 initialization code.
    """
    startRange = 147981
    endRange = 691423
    count = 0
    for number in range(endRange - startRange):
        number += startRange
        # Check conditions
        adjacentSame = False
        decreaseing = False
        previousNumber = 0
        for i in range(5):
            lastNumber = number % 10
            number //= 10
            #print(number, ' ', lastNumber)
            if lastNumber == number % 10 and number % 10 != number//10%10 and previousNumber != lastNumber:
                adjacentSame = True
            if lastNumber < number % 10:
                decreaseing = True
                break
            previousNumber = lastNumber
        if adjacentSame and not decreaseing:
            count += 1

    print(count)

challenge2()
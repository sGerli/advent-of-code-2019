import sys
from random import randrange

def openFile():
    return open(sys.argv[1], "r")

def processIntcode(data):
    pointer = 0
    while data[pointer] != 99:
        if (data[pointer] == 1):
            data[data[pointer + 3]] = data[data[pointer + 1]] + data[data[pointer + 2]]
        elif (data[pointer] == 2):
            data[data[pointer + 3]] = data[data[pointer + 1]] * data[data[pointer + 2]]
        else:
            print(str(data[pointer]) + " failed")
            break
        pointer += 4
    return data

def challenge1():
    """
    Create intcode processor and process input with 1202 initialization code.
    """
    file = openFile()
    data = list(map(lambda x: int(x), file.read().split(',')))
    data[1] = 12
    data[2] = 2
    processIntcode(data)
    print(data[0])
    file.close()

def challenge2(goal):
    """
    Find initialization code to get a goal output.
    """
    file = openFile()
    data = list(map(lambda x: int(x), file.read().split(',')))
    noun = verb = output = i = 0
    tested = {}
    while output != goal:
        thisData = data.copy()
        # Prevent having more than 10000 iterations
        while tested.get(100*noun + verb, None) is True:
        	noun = randrange(0, 99)
        	verb = randrange(0, 99)
        tested[100 * noun + verb] = True
        thisData[1] = noun
        thisData[2] = verb
        processIntcode(thisData)
        output = thisData[0]
        i+=1
    print(100*noun + verb)
    print(i)
    file.close()

challenge1()
challenge2(19690720)

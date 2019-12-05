import sys

def openFile():
    return open(sys.argv[1], "r")

def processIntcode(data):
    pointer = 0
    while data[pointer] != 99:
        opcode = int(str(data[pointer])[-2:])
        paramModes = str(data[pointer])[:-2]
        if (opcode == 1): # OPCODE 01 - Sum
            data[data[pointer + 3]] = getIntcodeParam(paramModes,data,pointer,1) + getIntcodeParam(paramModes,data,pointer,2)
            pointer += 4
        elif (opcode == 2): # OPCODE 02 - Multiply
            data[data[pointer + 3]] = getIntcodeParam(paramModes,data,pointer,1) * getIntcodeParam(paramModes,data,pointer,2)
            pointer += 4
        elif (opcode == 3):  # OPCODE 03 - Input
            data[data[pointer + 1]] = int(input("Type int: "))
            pointer += 2
        elif (opcode == 4):  # OPCODE 04 - Print
            print(getIntcodeParam(paramModes,data,pointer,1))
            pointer += 2
        # Start of part 2
        elif (opcode == 5):  # OPCODE 05 - JNZ (jump if not zero)
            if (getIntcodeParam(paramModes,data,pointer,1) != 0):
                pointer = getIntcodeParam(paramModes,data,pointer,2)
            else:
                pointer += 3
        elif (opcode == 6):  # OPCODE 06 - JZ (jump if zero)
            if (getIntcodeParam(paramModes,data,pointer,1) == 0):
                pointer = getIntcodeParam(paramModes,data,pointer,2)
            else:
                pointer += 3
        elif (opcode == 7):  # OPCODE 07 - Set 1 if first is less than second else 0
            if (getIntcodeParam(paramModes,data,pointer,1) < getIntcodeParam(paramModes,data,pointer,2)):
                data[data[pointer + 3]] = 1
            else:
                data[data[pointer + 3]] = 0
            pointer += 4
        elif (opcode == 8):  # OPCODE 08 - Set 1 if first is equal to second else 0
            if (getIntcodeParam(paramModes,data,pointer,1) == getIntcodeParam(paramModes,data,pointer,2)):
                data[data[pointer + 3]] = 1
            else:
                data[data[pointer + 3]] = 0
            pointer += 4
        else:
            print(str(data[pointer]) + " Something went wrong :(")
            break
        
    return data

def getIntcodeParam(paramModes, data, pointer, param):
    type = 0
    try:
        type = int(paramModes[-param])
    except:
        pass
    if (type == 0):
        return data[data[pointer + param]]
    else:
        return data[pointer + param]

def intcodeMachine():
    """
    Intcode processor that reads from file for AOC day 5
    """
    file = openFile()
    data = list(map(lambda x: int(x), file.read().split(',')))
    processIntcode(data)
    file.close()


intcodeMachine()

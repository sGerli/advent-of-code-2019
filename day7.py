import sys
import itertools

VERBOSE = False

def openFile():
    return open(sys.argv[1], "r")
class IntcodeMachine:
    def __init__(self, data):
        self.memory = data
        self.pointer = 0
        self.size = len(data)
        self.out = 0
        self.halt = False
        self.initialized = False

    def process(self, inputArg = None):
        if inputArg != None:  
            self.initialized = True
        
        while self.pointer < self.size:
            opcode = int(str(self.memory[self.pointer])[-2:])
            paramModes = str(self.memory[self.pointer])[:-2]
            if (opcode == 99): # HALT
                self.halt = True
                break
            elif (opcode == 1): # OPCODE 01 - Sum
                self.memory[self.memory[self.pointer + 3]] = self.getParam(paramModes,1) + self.getParam(paramModes,2)
                self.pointer += 4
            elif (opcode == 2): # OPCODE 02 - Multiply
                self.memory[self.memory[self.pointer + 3]] = self.getParam(paramModes,1) * self.getParam(paramModes,2)
                self.pointer += 4
            elif (opcode == 3):  # OPCODE 03 - Input
                if inputArg != None:
                    self.memory[self.memory[self.pointer + 1]] = inputArg
                    inputArg = None
                else:
                    if VERBOSE:
                        self.memory[self.memory[self.pointer + 1]] = int(input("Type int > "))
                    else:
                        break
                self.pointer += 2
            elif (opcode == 4):  # OPCODE 04 - Print
                out = self.getParam(paramModes,1)
                if VERBOSE:
                    print(">> " + str(out))
                self.out = out
                self.pointer += 2
            # Start of part 2
            elif (opcode == 5):  # OPCODE 05 - JNZ (jump if not zero)
                if (self.getParam(paramModes,1) != 0):
                    self.pointer = self.getParam(paramModes,2)
                else:
                    self.pointer += 3
            elif (opcode == 6):  # OPCODE 06 - JZ (jump if zero)
                if (self.getParam(paramModes,1) == 0):
                    self.pointer = self.getParam(paramModes,2)
                else:
                    self.pointer += 3
            elif (opcode == 7):  # OPCODE 07 - Set 1 if first is less than second else 0
                if (self.getParam(paramModes,1) < self.getParam(paramModes,2)):
                    self.memory[self.memory[self.pointer + 3]] = 1
                else:
                    self.memory[self.memory[self.pointer + 3]] = 0
                self.pointer += 4
            elif (opcode == 8):  # OPCODE 08 - Set 1 if first is equal to second else 0
                if (self.getParam(paramModes,1) == self.getParam(paramModes,2)):
                    self.memory[self.memory[self.pointer + 3]] = 1
                else:
                    self.memory[self.memory[self.pointer + 3]] = 0
                self.pointer += 4
            else:
                print(str(self.memory[self.pointer]) + " Something went wrong :(")
                break

    def getParam(self, paramModes, param):
        type = 0
        try:
            type = int(paramModes[-param])
        except:
            pass
        if (type == 0):
            return self.memory[self.memory[self.pointer + param]]
        else:
            return self.memory[self.pointer + param]

def run(data, range):
    permutations = list(itertools.permutations(range, len(range)))
    maxOutput = 0
    for permutation in permutations:
        machines = [IntcodeMachine(data.copy()) for x in permutation]
        current = 0
        previous = 4
        while not machines[current].halt:
            if not machines[current].initialized:
                inputArg = permutation[current]
            else:
                inputArg = machines[previous].out
            machines[current].process(inputArg)
            previous = current
            if current == len(permutation) - 1:
                current = 0
            else:
                current += 1
        maxOutput = max(maxOutput, machines[-1].out)

    return maxOutput

def challenges():
    """
    What is the highest signal that can be sent to the thrusters?
    """
    file = openFile()
    data = list(map(lambda x: int(x), file.read().split(',')))
    print("Challenge 1:", run(data, range(5)))
    print("Challenge 2:", run(data, range(5, 10)))
    file.close()

challenges()
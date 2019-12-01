import sys
from functools import reduce

def openFile():
    return open(sys.argv[1], "r")

def challenge1():
    """
    Calculate fuel required to launch a given module is based on its mass.
    Specifically, to find the fuel required for a module, take its mass,
    divide by three, round down, and subtract 2.
    """
    file = openFile()
    byLine = file.readlines()
    totalFuel = reduce(lambda prev, mass: prev + (int(mass)//3 - 2), byLine, 0)
    print(totalFuel)
    file.close()

def calculateModuleFuel(mass):
    """
    Calculate fuel requirement for a challenge 2 module.
    """
    moduleFuel = 0
    while True:
        fuel = int(mass)//3 - 2
        if fuel > 0:
            moduleFuel += fuel
            mass = fuel
        else:
            break
    return moduleFuel

def challenge2():
    """
    For each module mass, calculate its fuel and add it to the total.
    Then, treat the fuel amount you just calculated as the input mass
    and repeat the process, continuing until a fuel requirement is zero or negative.
    """
    file = openFile()
    byLine = file.readlines()
    totalFuel = reduce(lambda prev, mass: prev + calculateModuleFuel(mass), byLine, 0)
    print(totalFuel)
    file.close()

challenge1()
challenge2()
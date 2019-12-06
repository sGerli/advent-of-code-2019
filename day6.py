import sys
from random import randrange

def openFile():
    return open(sys.argv[1], "r")

def getOrbits(orbits, name, count = 0):
    newCount = count
    for planet in orbits[name]:
        newCount += getOrbits(orbits, planet, count + 1)
    return newCount

def challenge1():
    """
    What is the total number of direct and indirect orbits in your map data?
    """
    file = openFile()
    orbits = {'COM': []}
    byLine = file.readlines()
    for line in byLine:
        line = line.replace('\n','')
        data = line.split(')')
        if orbits.get(data[0], None) is not None:
            orbits[data[0]].append(data[1])
        else:
            orbits[data[0]] = [data[1]]
        
        if orbits.get(data[1], None) is None:
            orbits[data[1]] = []
    # Get orbit count
    print(getOrbits(orbits, 'COM'))
    file.close()


def getOrbitsFromTo(orbits, fromO, to, previous = None):
    oFrom = orbits[fromO]
    toSearch = []
    toSearch += oFrom['childs']
    if oFrom['parent'] is not None:
        toSearch.append(oFrom['parent'])
    if previous is not None:
        toSearch.remove(previous)
    if to in toSearch:
        return 1
    for orbit in toSearch:
        nc = getOrbitsFromTo(orbits, orbit, to, fromO)
        if nc > 0:
            return nc + 1
    return 0

def challenge2():
    """
    What is the minimum number of orbital transfers required to move from the object YOU
    are orbiting to the object SAN is orbiting? (Between the objects they are orbiting - not between YOU and SAN.)
    """
    file = openFile()
    orbits = {'COM': {'childs': [], 'parent': None}}
    byLine = file.readlines()
    for line in byLine:
        line = line.replace('\n','')
        data = line.split(')')
        if orbits.get(data[0], None) is not None:
            orbits[data[0]]['childs'].append(data[1])
        else:
            orbits[data[0]] = {'childs': [data[1]], 'parent': data[0]}
        
        if orbits.get(data[1], None) is None:
            orbits[data[1]] = {'childs': [], 'parent': data[0]}
        else:
            orbits[data[1]]['parent'] = data[0]
    # Get orbit count
    print(getOrbitsFromTo(orbits, 'YOU', 'SAN') - 2)
    file.close()
        


    

challenge2()

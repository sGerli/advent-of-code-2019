import sys
from math import atan2, pi
from collections import OrderedDict

def openFile():
    return open(sys.argv[1], "r")
    #return open("day101.txt", "r")

def readAsteroids(data):
    asteroids = {}
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '#':
                asteroids[(x, y)] = 0
    return asteroids

def challenge1():
    """
    Find best location for monitoring station
    """
    file = openFile()
    data = list(map(lambda data: list(data.replace('\n', '')), file.readlines()))
    asteroids = readAsteroids(data)

    # Find count of lines of sight
    maxSightCount = 0
    point = (0,0)
    for a in asteroids.keys():
        q = {}
        for posibility in asteroids.keys():
            x = posibility[0] - a[0]
            y = a[1] - posibility[1]
            slope = atan2(y, x)
            q[slope] = True

        sightCount = len(q)
        asteroids[a] = sightCount
        if (sightCount > maxSightCount):
            maxSightCount = sightCount
            point = a
    print(maxSightCount, point)
    file.close()

def challenge2(a):
    """
    Find 200th asteroid to get destroyed
    """
    file = openFile()
    data = list(map(lambda data: list(data.replace('\n', '')), file.readlines()))
    asteroids = readAsteroids(data)

    q = {}
    for posibility in asteroids.keys():
        if posibility == a:
            continue
        x = posibility[0] - a[0]
        y = a[1] - posibility[1]
        slope = atan2(y, x)
        if q.get(slope, None) == None:
            q[slope] = [(posibility[0],posibility[1])]
        else:
            q[slope] += [(posibility[0],posibility[1])]
    for slope in q:
        q[slope].sort(key=lambda v: abs(a[0] - v[0]) + abs(a[1] - v[1]))

    counter = 0
    orderedQ = sorted(q.items(), key= lambda v: v[0] if v[0] <= pi/2 else v[0]-(3*pi), reverse=True)
    while counter < 200:
        for slope in orderedQ:
            if len(slope[1]) > 0:
                counter += 1
                if counter == 200:
                    print(slope[1][0][0] * 100 + slope[1][0][1])
                    break
                slope[1].pop(0)
    
    file.close()

#challenge1()
challenge2((26, 28))
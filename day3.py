import sys

def openFile():
    return open(sys.argv[1], "r")

def findIntersections(byLine):
    boards = [{} for x in range(len(byLine))]
    boardIndex = 0
    for line in byLine: 
        movements = line.split(',')
        x = 0
        y = 0
        steps = 0
        for mov in movements:
            positions = int(mov[1:])
            if mov[0] == 'R':
                x, steps = drawHorizontal(boards[boardIndex], x, y, positions, steps)
            elif mov[0] == 'L':
                x, steps = drawHorizontal(boards[boardIndex], x, y, -positions, steps)
            elif mov[0] == 'U':
                y, steps = drawVertical(boards[boardIndex], x, y, positions, steps)
            elif mov[0] == 'D':
                y, steps = drawVertical(boards[boardIndex], x, y, -positions, steps)
            else:
                print('failed')
        boardIndex +=1
    return boards, boards[0].keys() & boards[1].keys()

def challenge1():
    """
    Closest wire intersection in manhattan distance to center
    """
    file = openFile()
    byLine = file.readlines()
    _, intersections = findIntersections(byLine)
    smallestDistance = float('Inf')
    for intersection in intersections:
        distance = abs(intersection[0]) + abs(intersection[1])
        if distance < smallestDistance:
            smallestDistance = distance
            closestIntersection = intersection
    print(smallestDistance)
    file.close()

def challenge2():
    """
    Find initialization code to get a goal output.
    """
    file = openFile()
    byLine = file.readlines()
    boards, intersections = findIntersections(byLine)
    minInterSteps = float("Inf")
    for intersection in intersections:
        combSteps = boards[0][intersection] + boards[1][intersection]
        if (combSteps < minInterSteps):
            minInterSteps = combSteps
    print(minInterSteps)
        
    file.close()

def drawHorizontal(board, startX, startY, movements, steps):
    endX = startX
    multiplier = -1 if movements < 0 else 1
    startX +=  multiplier * 1
    for x in range(abs(movements)):
        steps += 1
        endX = startX + multiplier * x
        board[(endX, startY)] = steps
    return endX, steps

def drawVertical(board, startX, startY, movements, steps):
    endY = startY
    multiplier = -1 if movements < 0 else 1
    startY += multiplier * 1
    for y in range(abs(movements)):
        steps += 1
        endY = startY + multiplier * y
        board[(startX, endY)] = steps
    return endY, steps

challenge1()
challenge2()
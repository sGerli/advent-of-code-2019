import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
MATRIX_SIZE=20480

def openFile():
    return open(sys.argv[1], "r")

def drawHorizontal(board, startX, startY, movements):
    endX = startX + movements
    if movements < 0:
        startX += movements
        movements = abs(movements)
        endX = startX
    else:
        startX += 1
    for x in range(movements):
        board[startY][startX + x] = '-'
    return endX

def drawVertical(board, startX, startY, movements):
    endY = startY + movements
    if movements < 0:
        startY += movements
        movements = abs(movements)
        endY = startY
    else:
        startY += 1
    for y in range(movements):
        board[startY + y][startX] = '|'
    return endY

def challenge1():
    """
    Closest wire intersection in manhattan distance to center
    """
    file = openFile()
    byLine = file.readlines()
    boards = [np.full((MATRIX_SIZE, MATRIX_SIZE), '.') for x in range(len(byLine))]
    for board in boards:
        board[MATRIX_SIZE//2][MATRIX_SIZE//2] = 'o'
    boardIndex = 0
    for line in byLine: 
        movements = line.split(',')
        x = MATRIX_SIZE//2
        y = MATRIX_SIZE//2
        for mov in movements:
            positions = int(mov[1:])
            if mov[0] == 'R':
                x = drawHorizontal(boards[boardIndex], x, y, positions)
            elif mov[0] == 'L':
                x = drawHorizontal(boards[boardIndex], x, y, -positions)
            elif mov[0] == 'U':
                
                y = drawVertical(boards[boardIndex], x, y, -positions)
            elif mov[0] == 'D':
                y = drawVertical(boards[boardIndex], x, y, positions)
            else:
                print('failed')
        # print(np.matrix(boards[boardIndex]))
        boardIndex +=1
    intersections = []
    for i in range(len(boards) - 1):
        for y in range(len(boards[i + 1])):
            row = boards[i + 1][y]
            orRow = boards[0][y]
            for z in range(len(row)):
                item = row[z]
                orItem = orRow[z]
                if (item == '-' and orItem == '|') or (item == '|' and orItem == '-'):
                    intersections += [(z, y)]
    smallestDistance = float('Inf')
    for intersection in intersections:
        distance = abs(MATRIX_SIZE//2 - intersection[0]) + abs(MATRIX_SIZE//2 - intersection[1])
        if distance < smallestDistance:
            smallestDistance = distance
            closestIntersection = intersection
    print(smallestDistance)
    print(closestIntersection)
        
    file.close()

challenge1()
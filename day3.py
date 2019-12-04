import sys
from random import randrange
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
MATRIX_SIZE=20480

def openFile():
    return open(sys.argv[1], "r")

def challenge1():
    """
    Create intcode processor and process input with 1202 initialization code.
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

"""
for mov in movements:
            positions = int(mov[1:])
            if mov[0] == 'R':
                extension = lastPos[0] + positions - len(board[0]) + 1
                if extension > 0:
                    # Extend to the rigth
                    for row in board:
                        row += ['' for i in range(extension)]

            elif mov[0] == 'L':
                extension = lastPos[0] - positions
                if extension < 0:
                    extension = abs(extension)
                    # Extend to the left
                    initialPos = (initialPos[0] + extension, initialPos[1])
                    for row in board:
                        row = ['' for i in range(extension)] + row


            elif mov[0] == 'U':
                extension = lastPos[1] - positions
                if extension < 0:
                    extension = abs(extension)
                    # Extend to the rigth
                    initialPos = (initialPos[0], initialPos[1] + extension)
                    board = [['' for y in range(len(board[0]))] for i in range(extension)] + board

            elif mov[0] == 'D':
                extension = lastPos[1] + positions - len(board) + 1
                if extension > 0:
                    # Extend to the rigth
                    board = [['' for y in range(len(board[0]))] for i in range(extension)] + board

            else:
                print('failed')
"""
def challenge2(goal):
    """
    Find initialization code to get a goal output.
    """
    file = openFile()
    data = list(map(lambda x: int(x), file.read().split(',')))
    output = 0
    while output != goal:
        thisData = data.copy()
        thisData[1] = noun = randrange(0, 99)
        thisData[2] = verb = randrange(0, 99)
        processIntcode(thisData)
        output = thisData[0]
    print(100*noun + verb)
    file.close()

challenge1()
#challenge2(19690720)
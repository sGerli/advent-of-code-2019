import sys

IMG_WIDTH = 25
IMG_HEIGHT = 6

def openFile():
    return open(sys.argv[1], "r")
    #return open("day81.txt", "r")

def challenge1():
    """
    Closest wire intersection in manhattan distance to center
    """
    file = openFile()
    inputData = list(map(int, list(file.read().replace("\n", ""))))

    zeroCount = float("Inf")
    result = 0
    while len(inputData) > 0:
        layer = inputData[:(IMG_WIDTH*IMG_HEIGHT)]
        inputData = inputData[(IMG_WIDTH*IMG_HEIGHT):]
        layerZeros = layer.count(0)
        if (layerZeros < zeroCount):
            zeroCount = layerZeros
            result = layer.count(1) * layer.count(2)

    print(result)
    
    file.close()

def challenge2():
    """
    Closest wire intersection in manhattan distance to center
    """
    file = openFile()
    inputData = list(map(int, list(file.read().replace("\n", ""))))
    layers = []
    while len(inputData) > 0:
        layer = []
        for i in range(IMG_HEIGHT):
            layer.append(inputData[:IMG_WIDTH])
            inputData = inputData[IMG_WIDTH:]
        layers.append(layer)
    
    topLayer = layers[0]
    layers = layers [1:]
    for y in range(len(topLayer)):
        for x in range(len(topLayer[y])):
            if topLayer[y][x] == 2:
                for layer in layers:
                    if layer[y][x] != 2:
                        topLayer[y][x] = layer[y][x]
                        break
    
    for y in range(len(topLayer)):
        print(''.join(list(map(lambda data: ' ' if data == 0 else '#' if data == 1 else "E", topLayer[y]))))
    
    file.close()

#challenge1()
challenge2()
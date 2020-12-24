def readFile(filepath):
    file = open(filepath, "r")
    lines = [line.strip("\n") for line in file.readlines()]
    stepList = []
    for line in lines:
        steps = []
        i = 0
        while i < len(line):
            if 's' == line[i]:
                steps.append(line[i:i + 2])
                i = i + 2
            elif 'n' == line[i]:
                steps.append(line[i:i + 2])
                i = i + 2
            else:
                steps.append(line[i])
                i = i + 1
        stepList.append(steps)
    return stepList


oddr_directions = [[[+1, 0], [0, -1], [-1, -1], [-1, 0], [-1, +1], [0, +1]],
                   [[+1, 0], [+1, -1], [0, -1], [-1, 0], [0, +1], [+1, +1]]]

directions = {'e': 0, 'ne': 1, 'nw': 2, 'w': 3, 'sw': 4, 'se': 5}


class OffsetCoord(object):
    def __init__(self, col, row):
        self.col = col
        self.row = row


def oddr_offset_neighbor(hex, direction):
    parity = hex.row & 1
    dir = oddr_directions[parity][directions[direction]]
    return OffsetCoord(hex.col + dir[0], hex.row + dir[1])


def getCoordinates(steps, referenceTile):
    startCoord = referenceTile
    for step in steps:
        startCoord = oddr_offset_neighbor(startCoord, step)
    return startCoord


def day24P1(stepList):
    tiles = dict()
    referenceTile = OffsetCoord(0, 0)
    for steps in stepList:
        coord = getCoordinates(steps, referenceTile)
        pos = tuple([coord.col, coord.row])
        if pos in tiles:
            tiles[pos] = not tiles[pos]
        else:
            tiles[pos] = True  # True: Black, False: White
    sumBlack = 0
    for tile in tiles:
        if tiles[tile]:
            sumBlack += 1
    return sumBlack


outter = 3


def getBound(floor):
    maxRow = maxCol = 0
    minRow = minCol = 1000000000
    for tile in floor:
        [col, row] = list(tile)
        maxCol = max(maxCol, col)
        minCol = min(minCol, col)
        maxRow = max(maxRow, row)
        minRow = min(minRow, row)
    return [maxRow, minRow, maxCol, minCol]


def updateFloor(floor, changeList):
    for tile in changeList:
        floor[tuple(tile)] = not floor[tuple(tile)]


def extendFloor(floor):
    [maxRow, minRow, maxCol, minCol] = getBound(floor)
    extFloor = dict()
    rowDim = maxRow - minRow
    colDim = maxCol - minCol
    # 初始化new地板
    ext = outter * 2
    for i in range(rowDim + ext):
        for j in range(colDim + ext):
            extFloor[tuple([minRow - outter + i, minCol - outter + j])] = False
    for tile in floor:
        extFloor[tile] = floor[tile]
    return extFloor


def numBlackNeibor(coord, floor):
    parity = coord[1] & 1  # coord.row & 1
    direction = oddr_directions[parity]
    numBlack = 0
    for dir in direction:
        pos = tuple([coord[0] + dir[0], coord[1] + dir[1]])
        if pos in floor and floor[pos]:
            numBlack += 1
    return numBlack


def getChangeList(floor):
    changeList = []
    for tile in floor:
        coord = list(tile)
        black = floor[tile]  # True: black, False: white
        num = numBlackNeibor(coord, floor)
        if black and (num == 0 or num > 2):
            changeList.append(coord)
        elif not black and num == 2:
            changeList.append(coord)
    return changeList


def numBlack(floor):
    # 计算黑色瓷砖的个数
    sumBlack = 0
    for f in floor:
        if floor[f]:
            sumBlack += 1
    return sumBlack


def day24P2(stepList):
    tiles = dict()
    referenceTile = OffsetCoord(0, 0)
    for steps in stepList:
        coord = getCoordinates(steps, referenceTile)
        pos = tuple([coord.col, coord.row])
        if pos in tiles:
            tiles[pos] = not tiles[pos]
        else:
            tiles[pos] = True  # True: Black, False: White
    sumBlack = 0

    floor = extendFloor(tiles)
    print("Init black tiles: ", numBlack(floor))
    # 更新地板
    sumBlack = 0
    for day in range(100):
        changeList = getChangeList(floor)
        updateFloor(floor, changeList)
        floor = extendFloor(floor)
        sumBlack = numBlack(floor)
        print(f"day {day+1}: {sumBlack}")

    return sumBlack


if __name__ == "__main__":
    stepList = readFile("./input")
    value = day24P2(stepList)

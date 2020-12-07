def day3P1(filepath):
    file = open(filepath, "r")
    lines = [line.strip("\n") for line in file.readlines()]
    numRows = len(lines)
    numCols = len(lines[0])
    currentCol = 0
    currentRow = 0
    numTrees = 0
    numSquare = 0
    for i in range(numRows):
        currentRow = currentRow + 1
        if currentRow >= numRows:
            break
        currentCol = (currentCol + 3) % numCols

        line = lines[currentRow]
        if line[currentCol] == '#':
            numTrees = numTrees + 1
        else:
            numSquare = numSquare + 1
    return numTrees


def day3P2(filepath, right, down):
    file = open(filepath, "r")
    lines = [line.strip("\n") for line in file.readlines()]
    numRows = len(lines)
    numCols = len(lines[0])
    currentCol = 0
    currentRow = 0
    numTrees = 0
    numSquare = 0
    for i in range(numRows):
        currentCol = (currentCol + right) % numCols
        currentRow = currentRow + down
        if currentRow >= numRows:
            break
        line = lines[currentRow]
        if line[currentCol] == '#':
            numTrees = numTrees + 1
        else:
            numSquare = numSquare + 1
    return numTrees


if __name__ == "__main__":
    print("day3 problem 1: ", day3P1("./input"))
    r1d1 = day3P2("./input", 1, 1)
    r3d1 = day3P2("./input", 3, 1)
    r5d1 = day3P2("./input", 5, 1)
    r7d1 = day3P2("./input", 7, 1)
    r1d2 = day3P2("./input", 1, 2)
    print("day3 problem 2: ", r1d1 * r3d1 * r5d1 * r7d1 * r1d2)

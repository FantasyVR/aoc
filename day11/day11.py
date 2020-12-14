directions = []
for i in range(-1, 2):
    for j in range(-1, 2):
        directions.append([i, j])
directions.remove([0, 0])

step = lambda loc, direction: [loc[0] + direction[0], loc[1] + direction[1]]


def readFile(filepath):
    file = open(filepath, "r")
    lines = [line.strip("\n") for line in file.readlines()]
    return lines


def change(seats, row, col):
    numEmpty = 0
    numFloor = 0
    numOccupied = 0
    isEdage = False
    isCorner = False

    startRow = row - 1
    endRow = row + 1
    startCol = col - 1
    endCol = col + 1
    if startRow < 0:
        startRow = 0
        isEdage = True
    if endRow > len(seats) - 1:
        endRow = len(seats) - 1
        isEdage = True
    if startCol < 0:
        startCol = 0
        isEdage = True
    if endCol > len(seats[0]) - 1:
        endCol = len(seats[0]) - 1
        isEdage = True
    if (row == 0 and col == 0) or (row == 0 and col == len(seats[0]) - 1) or (row == len(seats) - 1 and col == 0) or (
            row == len(seats) - 1 and col == len(seats[0]) - 1):
        isCorner = True
        isEdage = False

    for i in range(startRow, endRow + 1):
        for j in range(startCol, endCol + 1):
            if seats[i][j] == "L":
                numEmpty += 1
            elif seats[i][j] == ".":
                numFloor += 1
            elif seats[i][j] == "#":
                numOccupied += 1

    if seats[row][col] == "L":
        if isCorner and numEmpty + numFloor == 4:
            return True
        elif isEdage and numEmpty + numFloor == 6:
            return True
        elif numEmpty + numFloor == 9:
            return True
        else:
            return False
    elif seats[row][col] == "#":
        if numOccupied > 4:
            return True
    else:
        return False


def day11P1(seats):
    numCols = len(seats[0])
    numRows = len(seats)
    nextSeats = [seat for seat in seats]
    for i in range(numRows):
        for j in range(numCols):
            if change(seats, i, j):
                if seats[i][j] == '#':  # occupied
                    s = list(nextSeats[i])
                    s[j] = 'L'
                    nextSeats[i] = ''.join(s)
                elif seats[i][j] == 'L':
                    s = list(nextSeats[i])
                    s[j] = '#'
                    nextSeats[i] = ''.join(s)
    return nextSeats




def findOccupied(seats, row, col):
    numEmpty = 0
    for direction in directions:
        [r, c] = step([row, col], direction)
        while (0 <= r < len(seats) ) and (0 <= c < len(seats[0])):
            if seats[r][c] == "#":
                return True
            elif seats[r][c] == "L":
                break
            else:
                [r, c] = step([r, c], direction)
    return False

def numOccupied(seats, row, col):
    numEmpty = 0
    for direction in directions:
        [r, c] = step([row, col], direction)
        while (0 <= r < len(seats) ) and (0 <= c < len(seats[0])):
            if seats[r][c] == "#":
                numEmpty += 1
                break
            elif seats[r][c] == "L":
                break
            else:
                [r, c] = step([r, c], direction)
    return numEmpty

def countNeibor(seats, row, col):
    numNeibors = 0
    for direction in directions:
        [r,c] = step([row, col], direction)
        if (0 <= r < len(seats)) and (0 <= c < len(seats[0])):
            numNeibors += 1
    return numNeibors


def day11P2(seats):
    nextSeats = [seat for seat in seats]

    numRows = len(seats)
    numCols = len(seats[0])
    for i in range(numRows):
        for j in range(numCols):
            if seats[i][j] == "L":
                if not findOccupied(seats,i,j):
                    s = list(nextSeats[i])
                    s[j] = '#'
                    nextSeats[i] = ''.join(s)
            elif seats[i][j] == "#":
                if numOccupied(seats, i, j) >= 5:
                    s = list(nextSeats[i])
                    s[j] = 'L'
                    nextSeats[i] = ''.join(s)
    return nextSeats


if __name__ == "__main__":
    seats = readFile("./input")
    count = 0
    for i in range(100):
        #nextSeats = day11P1(seats)
        nextSeats = day11P2(seats)
        if seats == nextSeats:
            for seat in nextSeats:
                for s in seat:
                    if s == "#":
                        count += 1
            print(nextSeats)
            print("right: ", count)
            break
        seats = nextSeats
        print(nextSeats)

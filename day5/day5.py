import math
def getSID(line):
    if len(line) != 10:
        print("wrong seat number")
        return -1
    row = 0
    col = 1
    f = 0
    b = 127
    l = 0
    r = 7
    for i in range(6):
        if line[i] == 'F':
            b = math.floor((f+b)/2.0)
        elif line[i] == 'B':
            f = math.ceil((f+b)/2.0)
    if line[6] == 'F':
        row = f
    elif line[6] == 'B':
        row = b
    for i in range(2):
        if line[i+7] == 'L':
            r = math.floor((l+r)/2)
        elif line[i+7] == 'R':
            l = math.ceil((l+r)/2)
    if line[9] == 'L':
        col = l
    elif line[9] == 'R':
        col = r
    return row * 8 + col

def day5P1(filepath):
    file = open(filepath, "r")
    lines = file.readlines()
    hSID = 0;
    for line in lines:
        SID = getSID(line.strip("\n"))
        if SID > hSID:
            hSID = SID
    return hSID

def day5P2(filepath):
    file = open(filepath, "r")
    lines = file.readlines()
    idList = []
    for i in range(len(lines)):
        SID = getSID(lines[i].strip("\n"))
        idList.insert(i, SID)
    numSeats = 128 * 8;
    for i in range(numSeats):
        if i not in idList:
            if i > 100 and i < 900:
                print(i)

if __name__ == "__main__":
    print(day5P1("./input"))
    day5P2("./input")
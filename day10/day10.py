def day10P1(filepath):
    file = open(filepath,"r")
    lines = [int(line.strip("\n")) for line in file.readlines()]
    voltList = sorted(lines)
    diff1 = 0
    diff3 = 0
    start = 0
    for i in range(len(voltList)):
        if voltList[i] - start == 1:
            diff1 += 1
        elif voltList[i] - start == 3:
            diff3 += 1
        start = voltList[i]
    return diff1 * (diff3+1)
def day10P2(filepath):
    file = open(filepath,"r")
    lines = [int(line.strip("\n")) for line in file.readlines()]
    voltList = sorted(lines)
    voltList = [0] + voltList + [voltList[len(voltList)-1]+3]
    diff = []
    for i in range(1,len(voltList)):
        diff += [voltList[i] - voltList[i-1]]

    continus = []
    fragment = 0
    for i in range(len(diff)):
        if diff[i] == 3:
            continus.append(fragment)
            fragment = 0
        elif diff[i] == 1:
            fragment += 1
    count = 1
    for c in continus:
        if c == 2:
            count *=2
        elif c == 3:
            count *=4
        elif c == 4:
            count *= 7
    return count

if __name__ == "__main__":
    #p1 = day10P1("./input")
    value = day10P2("./input")
    print(value)
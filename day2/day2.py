def day2P1(filepath):
    file = open(filepath, "r")
    lines = file.readlines()
    numValid = 0
    for line in lines:
        parts = line.split(" ")
        lower = int(parts[0].split('-')[0])
        upper = int(parts[0].split('-')[1])
        zimu = parts[1][0]
        numCount = parts[2].count(zimu)
        if numCount < lower or numCount > upper:
            continue
        else:
            numValid = numValid + 1
    return numValid


def day2P2(filepath):
    file = open(filepath, "r")
    lines = file.readlines()
    numValid = 0
    for line in lines:
        parts = line.split(" ")

        lower = int(parts[0].split('-')[0]) - 1
        upper = int(parts[0].split('-')[1]) - 1
        zimu = parts[1][0]
        string = parts[2]
        if string[lower] == zimu or string[upper] == zimu:
            if string[lower] == zimu and string[upper] == zimu:
                continue
            else:
                numValid = numValid + 1

    return numValid


if __name__ == "__main__":
    numValid = day2P1("./input")
    print("day 2 Problem 1", numValid)
    numValid = day2P2("./input")
    print("day 2 Problem 2", numValid)

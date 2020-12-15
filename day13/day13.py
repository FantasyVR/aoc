def readFile(filepath):
    file = open(filepath,"r")
    lines = [line.strip("\n") for line in file.readlines()]
    time = int(lines[0])
    busList = lines[1].split(",")
    validBusList = []
    for bus in busList:
        if bus != 'x':
            validBusList.append(int(bus))
    return time, validBusList

def day13P1(time, busList):
    minYu = int(10e6);
    minIndx = -1;
    for i in range(len(busList)):
        yu = busList[i] - time % busList[i]
        if yu < minYu:
            minYu = yu
            minIndx = i

    return busList[minIndx] * (minYu)

def day13P2(filepath):
    file = open(filepath,"r")
    lines = [line.strip("\n") for line in file.readlines()]
    busList = lines[1].split(",")
    validBusList = []
    for i in range(len(busList)):
        if busList[i] != 'x':
            validBusList.append([int(busList[i]),i])

    for i in range(100000000000000, 10000000000000000000):
        if i % validBusList[0][0] == 0:
            real = True
            for idx in range(1, len(validBusList)):
                if (validBusList[idx][0] - i % validBusList[idx][0]) == validBusList[idx][1]:
                    continue
                else:
                    real = False
                    break
            if real:
                print(i)
                return i


if __name__ == "__main__":
    # time, busList = readFile("./input")
    # value = day13P1(time, busList)
    # print(value)
    day13P2("./input")
def day16P1(filepath):
    numRangeList = []
    myTicket = []
    nearTickets = []
    file = open(filepath, "r")
    lines = [line.strip("\n") for line in file.readlines()]
    lines = [line for line in lines if line!='']
    row = 0
    for row in range(len(lines)):
        if "your ticket" in lines[row]:
            break
        line = lines[row]
        field = line.split(":")[0]
        numRange = line.split(":")[1]
        range1 = numRange.split("or")[0].strip(" ")
        lower = int(range1.split("-")[0])
        uppper = int(range1.split("-")[1])
        numRangeList.append([lower, uppper])
        range2 = numRange.split("or")[1].strip(" ")
        lower = int(range2.split("-")[0])
        uppper = int(range2.split("-")[1])
        numRangeList.append([lower, uppper])

    for i in range(row, len(lines)):
        if "your ticket" in lines[row]:
            myTicket = [int(x) for x in lines[row + 1].split(",")]
            break

    row = row + 2
    for i in range(row, len(lines)):
        if "nearby ticket" in lines[i]:
            continue
        ticket = [int(x) for x in lines[i].split(",")]
        nearTickets += ticket
    error = 0
    for ticket in nearTickets:
        if not isValid(numRangeList, ticket):
            error += ticket

    print(error)
    return error


def isValid(numRangeList, ticket):
    for numRange in numRangeList:
        if numRange[0] <= ticket <= numRange[1]:
            return True
    return False

def day16P2(filepath):
    numRangeList = []
    myTicket = []
    nearTickets = []
    file = open(filepath, "r")
    lines = [line.strip("\n") for line in file.readlines()]
    lines = [line for line in lines if line!='']
    row = 0
    fieldRange = dict()
    for row in range(len(lines)):
        if "your ticket" in lines[row]:
            break
        line = lines[row]
        field = line.split(":")[0]
        numRange = line.split(":")[1]
        range1 = numRange.split("or")[0].strip(" ")
        lower1 = int(range1.split("-")[0])
        upper1 = int(range1.split("-")[1])
        numRangeList.append([lower1, upper1])
        range2 = numRange.split("or")[1].strip(" ")
        lower2 = int(range2.split("-")[0])
        upper2 = int(range2.split("-")[1])
        numRangeList.append([lower2, upper2])
        fieldRange[field] = [[lower1,upper1], [lower2,upper2]]
    # 读取 my ticket numbers
    for i in range(row, len(lines)):
        if "your ticket" in lines[row]:
            myTicket = [int(x) for x in lines[row + 1].split(",")]
            break
    # 读取其他人的ticket数据
    row = row + 2
    for i in range(row, len(lines)):
        if "nearby ticket" in lines[i]:
            continue
        ticket = [int(x) for x in lines[i].split(",")]
        nearTickets.append(ticket)
    # 删除不符合条件的ticket中的数据
    for i in range(len(nearTickets)):
        validT = rmNonValid(numRangeList, nearTickets[i])
        nearTickets[i] = validT

    # 一个field可能适合多个column,那我们先确定每个field都适合哪些column
    # 需要注意的是，经过上一步的删除之后，ticket的长度可能发生了变化，最少19列，最多20列
    fieldIndex = dict()
    for col in range(len(nearTickets[0])-1):
        for field in fieldRange:
            correctField = True
            fRange = fieldRange[field]
            for row in range(len(nearTickets)):
                if not validRange(nearTickets[row][col], fRange):
                    correctField = False
                    break

            if correctField:
                if field in fieldIndex:
                    fieldIndex[field].append(col)
                else:
                    fieldIndex[field] = [col]
    # 第20列的数据都适用哪些field
    for field in fieldRange:
        fRange = fieldRange[field]
        correctField = True
        for row in range(len(nearTickets)):
            if len(nearTickets[row]) == 20:
                if not validRange(nearTickets[row][19], fRange):
                    correctField = False
                    break
        if correctField:
            if field in fieldIndex:
                fieldIndex[field].append(19)
            else:
                fieldIndex[field] = [19]
    # 排除法将field 和 column 对应起来
    fandI = dict()
    for i in range(20):
        for field in fieldIndex:
            if len(fieldIndex[field]) == 1:
                index = fieldIndex[field][0]
                fandI[field] = index
                for f in fieldIndex:
                    if index in fieldIndex[f]:
                        fieldIndex[f].remove(index)

    num = 1
    for f in fandI:
        if "departure" in f:
            idx = fandI[f]
            num *= myTicket[idx]
    return num
# 判断 ticket是否在范围之内， frange = [[a,b],[c,d]]
def validRange(ticket, frange):
    for r in frange:
        if r[0] <= ticket <= r[1]:
            return True
    return False


def rmNonValid(numRangeList, ticket):
    tmp =[t for t in ticket]
    for t in ticket:
        inRange = False
        for numRange in numRangeList:
            if numRange[0] <= t <= numRange[1]:
                inRange = True
                break
        if not inRange:
            tmp.remove(t)
    return tmp


if __name__ == "__main__":
    value = day16P1("./input")
    print(value)

    value = day16P2("./input")
    print(value)
startNums = [2,0,1,7,4,14,18]
def day15P1():
    turnNumber = [num for num in startNums]
    for i in range(len(startNums),30000000):
        if turnNumber[i-1] not in turnNumber[:i-1]:
            turnNumber.append(0)
        else:
            idx = i - 1
            for j in reversed(range(len(turnNumber[:i-1]))):
                if turnNumber[j] == turnNumber[idx]:
                    value = idx - j
                    turnNumber.append(value)
                    break
    return turnNumber[-1]

#print(day15P1())
startNums = [1,3,2]
def day15P2(count = 30000000):
    numIdxMap = dict()
    for i in range(len(startNums)-1):
        numIdxMap[startNums[i]] = i
    lastNumber = startNums[-1]
    for i in range(len(startNums)-1,count):
        if lastNumber not in numIdxMap:
            numIdxMap[lastNumber] = i
            lastNumber = 0
        else:
            value = i - numIdxMap[lastNumber]
            numIdxMap[lastNumber] = i
            lastNumber = value
    for num in numIdxMap:
        if numIdxMap[num] == count - 1:
            print(num)
            return num

print(day15P2())

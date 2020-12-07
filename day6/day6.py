

def getAnswer(groupInfo):
    aSet = set()
    for i in range(len(groupInfo)):
        if groupInfo[i] >='a' and groupInfo[i]  <= 'z':
            aSet.add(groupInfo[i])
    return len(aSet)

def day6P1(filepath):
    file = open(filepath,"r")
    lines = file.readlines()
    groupInfo = ""
    numPerson = 0
    answerCount = 0
    for i in range(len(lines)):
        if lines[i] == '\n':
            answer = getAnswer(groupInfo)
            answerCount += answer
            groupInfo = ""
            numPerson = 0
        else:
            groupInfo += lines[i].strip("\n")
            numPerson += 1

    answer = getAnswer(groupInfo)
    answerCount += answer

    return answerCount
def getRAnswer(groupInfo):
    realAnswer = dict()
    for person in groupInfo:
        aset = set()
        for a in person:
            aset.add(a)
        for a in aset:
            if a in realAnswer:
                realAnswer[a] += 1
            else:
                realAnswer[a] = 1
    count = 0
    for a in realAnswer:
        if realAnswer[a] == len(groupInfo):
            count += 1
    return count

def day6P2(filepath):
    file = open(filepath,"r")
    lines = file.readlines()
    groupInfo = []
    answerCount = 0
    for i in range(len(lines)):
        if lines[i] == '\n':
            answer = getRAnswer(groupInfo)
            answerCount += answer
            groupInfo = []
        else:
            groupInfo += [lines[i].strip("\n")]

    answer = getAnswer(groupInfo)
    answerCount += answer

    return answerCount


if __name__ == "__main__":
    print(day6P2("./input"))
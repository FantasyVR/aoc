import os
def day1(filepath):
    expense = open(filepath,"r")
    lines = [int(line) for line in expense.readlines()]
    for line in lines:
        value = line
        target = 2020 - value
        if(target in lines):
            return value * target
        else:
            continue
def day1P2(filepath):
    expense = open(filepath,"r")
    lines = [int(line) for line in expense.readlines()]
    numRows = len(lines)
    for i in range(numRows):
        value = lines[i]
        for j in range(i+1,numRows):
            startValue = lines[j]
            for k in reversed(range(j+1,numRows)):
                endValue = lines[k]
                sum = value + startValue + endValue
                if(sum == 2020):
                    return value * startValue * endValue

if __name__ == "__main__":
    value = day1P2("./input")
    print(value)
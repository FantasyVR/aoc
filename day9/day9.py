def isValid(numbers, num):
    for i in range(len(numbers)):
        target = num - numbers[i]
        if target in numbers and numbers.index(target) != i:
            return True
    return False
def day9P1(filepath):
    file = open(filepath,"r")
    numbers = [int(line.strip("\n")) for line in file.readlines()]
    step = 25
    for i in range(step, len(numbers)):
        if isValid(numbers[i-step:i], numbers[i]):
            continue
        else:
            resultList = day9P2(numbers, numbers[i])
            print("day 9 problem 2:", min(resultList) + max(resultList))
            return numbers[i]
    return None

def day9P2(numbers, target):
    for step in range(2,len(numbers)-1):
        for i in range(step, len(numbers)):
            numSum = sum(numbers[i-step:i])
            if numSum == target:
                return numbers[i-step:i]

if __name__ == "__main__":
    print("day 9 problem 1:", day9P1("./input"))

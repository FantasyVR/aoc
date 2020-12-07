import re
goal_bag_color = "shiny gold"
bagColorMap = dict()

def isValidBag(bag):
    colors = bagColorMap[bag]
    for color in colors:
        if goal_bag_color in color:
            return True
        else:
            if not isValidBag(color):
                continue
            else:
                return True
    return False

def day7P1(filepath):
    file = open(filepath,"r")
    lines = file.readlines()
    count = 0
    for line in lines:
        line = line.strip("\n")
        outterBag = re.findall("^[a-z]+ [a-z]+ bags", line)[0][:-5]
        innerBags = [i[2:-4] for i in re.findall('[0-9] [a-z]+ [a-z]+ bag', line)]

        if outterBag in bagColorMap:
            print("not right bag")
        else:
            bagColorMap[outterBag] = innerBags

    for bag in bagColorMap:
        if isValidBag(bag):
            count += 1
    return count

def getNum(bagColor):
    count = 0
    colors = bagColorMap[bagColor]
    for color in colors:
        count += color[0]
        count += color[0] * getNum(color[1])
    return count

def day7P2(filepath):
    file = open(filepath,"r")
    lines = file.readlines()
    count = 0
    for line in lines:
        line = line.strip("\n")
        outterBag = re.findall("^[a-z]+ [a-z]+ bags", line)[0][:-5]
        innerBags = [[int(i[:2]),i[2:-4]] for i in re.findall('[0-9] [a-z]+ [a-z]+ bag', line)]

        if outterBag in bagColorMap:
            print("not right bag")
        else:
            bagColorMap[outterBag] = innerBags

    return getNum(goal_bag_color)


if __name__ == "__main__":
    #print("day 7 problem 1: ", day7P1("./input"))
    print("day 7 problem 2: ", day7P2("./input"))
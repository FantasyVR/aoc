import math
def readFile(filepath):
    file = open(filepath,"r")
    lines = [line.strip("\n") for line in file.readlines()]
    return lines

def day12P1(instructions):
    loc = [0,0]
    dir = [1,0]
    for ins in instructions:
        cmd = ins[0]
        value = int(ins[1:])
        if cmd == 'F':
            loc = [value * dir[0] + loc[0], value * dir[1] + loc[1]]
        elif cmd == 'N':
            loc = [loc[0], loc[1]+value]
        elif cmd == 'S':
            loc = [loc[0], loc[1]-value]
        elif cmd == 'E':
            loc = [loc[0] + value, loc[1]]
        elif cmd == 'W':
            loc = [loc[0] - value, loc[1]]
        elif cmd == 'L':
            if value == 90:
                dir = [-dir[1], dir[0]]
            elif value == 180:
                dir = [-dir[0], -dir[1]]
            elif value == 270:
                dir = [dir[1],-dir[0]]
        elif cmd == 'R':
            if value == 90:
                dir = [dir[1], -dir[0]]
            elif value == 180:
                dir = [-dir[0], -dir[1]]
            elif value == 270:
                dir = [-dir[1],dir[0]]
        else:
            print("Wrong number")
    return math.fabs(loc[0]) + math.fabs(loc[1])
def day12P2(instructions, ):
    loc = [0,0]
    waypoint = [10, 1]
    for ins in instructions:
        cmd = ins[0]
        value = int(ins[1:])
        if cmd == 'F':
            loc = [value * waypoint[0] + loc[0], value * waypoint[1] + loc[1]]
        elif cmd == 'N':
            waypoint = [waypoint[0], waypoint[1]+value]
        elif cmd == 'S':
            waypoint = [waypoint[0], waypoint[1]-value]
        elif cmd == 'E':
            waypoint = [waypoint[0] + value, waypoint[1]]
        elif cmd == 'W':
            waypoint = [waypoint[0] - value, waypoint[1]]
        elif cmd == 'L':
            if value == 90:
                waypoint = [-waypoint[1], waypoint[0]]
            elif value == 180:
                waypoint = [-waypoint[0], -waypoint[1]]
            elif value == 270:
                waypoint = [waypoint[1],-waypoint[0]]
        elif cmd == 'R':
            if value == 90:
                waypoint = [waypoint[1], -waypoint[0]]
            elif value == 180:
                waypoint = [-waypoint[0], -waypoint[1]]
            elif value == 270:
                waypoint = [-waypoint[1],waypoint[0]]
        else:
            print("Wrong number")
    return math.fabs(loc[0]) + math.fabs(loc[1])

if __name__ == "__main__":
    instructions = readFile("./input")
    #value = day12P1(instructions)
    value = day12P2(instructions)
    print(value)
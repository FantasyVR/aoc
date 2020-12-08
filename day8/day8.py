def day8P1(filepath):
    file = open(filepath,"r")
    lines = file.readlines()
    acc = 0
    hitIns = []
    i = 0
    while i not in hitIns:
        instruction = lines[i].strip("\n")
        hitIns.append(i)
        operation = instruction[:3]
        args = instruction.split(" ")[1]
        isPlus = args[0]
        arg = int(args[1:])
        if operation == "nop":
            i += 1
        elif operation == "acc":
            if isPlus == "+":
                acc += arg
            elif isPlus == "-":
                acc -= arg
            i += 1
        elif operation == "jmp":
            if isPlus == "+":
                i += arg
            elif isPlus == "-":
                i -= arg
    return acc

# 目前的方法其实时候是有bug的，如果最后input最后一行有acc,那么输出的结果还需要加上这个acc的参数才行
def day8P2(filepath):
    file = open(filepath,"r")
    lines = [line.strip("\n") for line in file.readlines()]
    acc = 0
    terminate = len(lines) - 1
    wrongInsList = []
    for i in range(len(lines)):
        instruction = lines[i].strip("\n")
        operation = instruction[:3]
        if operation == "jmp" or operation == "nop":
            wrongInsList.append(i)
    hitIns = []
    i = 0
    for wrongIdx in range(len(wrongInsList)):
        while i not in hitIns:
            if i == terminate:
                return acc
            instruction = lines[i]
            hitIns.append(i)
            operation = instruction[:3]
            if i == wrongInsList[wrongIdx]:
                if operation == "nop":
                    operation = "jmp"
                elif operation == "jmp":
                    operation = "nop"

            args = instruction.split(" ")[1]
            isPlus = args[0]
            arg = int(args[1:])
            if operation == "nop":
                i += 1
            elif operation == "acc":
                if isPlus == "+":
                    acc += arg
                elif isPlus == "-":
                    acc -= arg
                i += 1
            elif operation == "jmp":
                if isPlus == "+":
                    i += arg
                elif isPlus == "-":
                    i -= arg
        hitIns = []
        i = 0
        acc = 0

if __name__ == "__main__":
    #print(day8P1("./input"))
    print(day8P2("./input"))
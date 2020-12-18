def readFile(filepath):
    file = open(filepath, "r")
    lines = [line.strip("\n") for line in file.readlines()]
    return lines


def infix2postfix(expression):
    postExp = []
    stack = []
    for i in range(len(expression)):
        if expression[i] == " ":
            continue
        elif '0' <= expression[i] <= '9':  # operand -> post expression
            postExp.append(expression[i])
        elif expression[i] in ['+', '-', '*', '/']:  # operator
            while len(stack) > 0 and stack[-1] != '(':
                postExp.append(stack[-1])
                stack = stack[:-1]
            stack.append(expression[i])
        elif expression[i] == '(':  # '(' -> stack
            stack.append('(')
        elif expression[i] == ')':  # ')'
            while len(stack) > 0 and stack[-1] != '(':
                postExp.append(stack[-1])
                stack = stack[:-1]
            if len(stack) > 0 and stack[-1] == '(':
                stack = stack[:-1]

    while len(stack) > 0:
        postExp.append(stack[-1])
        stack = stack[:-1]
    return postExp


precedence = {'*': 1, '+': 2}
def infix2postfix2(expression):
    postExp = []
    stack = []
    for i in range(len(expression)):
        if expression[i] == " ":
            continue
        elif '0' <= expression[i] <= '9':  # operand -> post expression
            postExp.append(expression[i])
        elif expression[i] in ['+', '-', '*', '/']:  # operator
            while len(stack) > 0 and stack[-1] != '(' and precedence[expression[i]] <= precedence[stack[-1]]:
                postExp.append(stack[-1])
                stack = stack[:-1]
            stack.append(expression[i])
        elif expression[i] == '(':  # '(' -> stack
            stack.append('(')
        elif expression[i] == ')':  # ')'
            while len(stack) > 0 and stack[-1] != '(':
                postExp.append(stack[-1])
                stack = stack[:-1]
            if len(stack) > 0 and stack[-1] == '(':
                stack = stack[:-1]

    while len(stack) > 0:
        postExp.append(stack[-1])
        stack = stack[:-1]
    return postExp


def evaluePostExp(postExp):
    stack = []
    for i in range(len(postExp)):
        if '0' <= postExp[i] <= '9':
            stack.append(postExp[i])
        else:
            a = int(stack[-1])
            b = int(stack[-2])
            re = 0
            if postExp[i] == '+':
                re = a + b
            elif postExp[i] == '-':
                re = a - b
            elif postExp[i] == '*':
                re = a * b
            elif postExp[i] == '/':
                re = a / b
            stack[-2] = re
            stack = stack[:-1]
    return stack[-1]


def day18P1(hws):
    sum = 0
    for hw in hws:
        exp = [l for l in hw if l != ' ']
        postExp = infix2postfix(exp)
        print(postExp)
        value = evaluePostExp(postExp)
        sum += value
    return sum

def day18P2(hws):
    sum = 0
    for hw in hws:
        exp = [l for l in hw if l != ' ']
        postExp = infix2postfix2(exp)
        print(postExp)
        value = evaluePostExp(postExp)
        sum += value
    return sum

if __name__ == "__main__":
    hws = readFile("./input")
    value = day18P2(hws)
    print(value)

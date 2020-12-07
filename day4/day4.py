import re
validOption = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def isValid(personInfo):
    keyValues = personInfo.split(" ")
    keys = [keyValue.split(":")[0] for keyValue in keyValues if keyValue != '']
    values = [
        keyValue.split(":")[1] for keyValue in keyValues if keyValue != ''
    ]
    for option in validOption:
        if option not in keys:
            return False
    for i in range(len(keys)):
        key = keys[i]
        value = values[i]
        if key == 'byr':
            if re.findall("^[0-9]{4}$", value) != [] and (int(value) < 1920 or int(value) > 2002):
                return False
        elif key == 'iyr':
            if re.findall("^[0-9]{4}$", value) != [] and (int(value) < 2010 or int(value) > 2020):
                return False
        elif key == 'eyr':
            if re.findall("^[0-9]{4}$", value) != [] and (int(value) < 2020 or int(value) > 2030):
                return False
        elif key == 'hgt':
            if value[-2:] == 'cm' and (int(value[:-2]) < 150
                                       or int(value[:-2]) > 193):
                return False
            elif value[-2:] == 'in' and (int(value[:-2]) < 59
                                         or int(value[:-2]) > 76):
                return False
            elif value[-2:] != 'cm' and value[-2:] != 'in':
                return False
        elif key == 'hcl':
            if not re.findall("^#[a-f|0-9]{6}$", value):
                return False
        elif key == 'ecl':
            color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if value not in color:
                return False
        elif key == 'pid':
            if not re.findall("^[0-9]{9}$", value):
                return False
    return True


def day4P2(filepath):
    file = open(filepath, "r")
    lines = file.readlines()
    personInfo = ""
    validCount = 0
    for line in lines:
        if line == "\n":
            if isValid(personInfo):
                validCount += 1
            personInfo = ""
        else:
            personInfo += " " + line.strip("\n")
    if isValid(personInfo):
        validCount += 1
    return validCount


if __name__ == "__main__":
    print(day4P2("./input"))

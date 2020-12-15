def readFile(filepath):
    file = open(filepath,"r")
    lines = [line.strip("\n") for line in file.readlines()]
    return lines

def value2bin(value, length):
    v = bin(value)
    sv = str(v)[2:]
    rv = ['0']*length
    startIdx = length - len(sv)
    for i in range(startIdx,length):
            rv[i] = sv[i-startIdx]
    return rv

def bin2value(binValue):
    return int(binValue, 2)

def computeValue(mask, value):
    v = value2bin(value, len(mask))
    for i in reversed(range(len(mask))):
        if mask[i] == 'X':
            continue
        else:
            v[i] = mask[i]
    sv = "".join(v)
    rv = bin2value(sv)
    return rv

def day14P1(instructions):
    mask = ""
    addressDict = dict()
    for ins in instructions:
        if "mask" in ins:
            mask = ins.split(" ")[2]
        elif "mem" in ins:
            b = [x.strip(" ") for x in ins.split("=")]
            address = b[0][4:-1]
            value = int(b[1])
            addressDict[address] = computeValue(mask, value)
    sum = 0
    for address in addressDict:
        sum += addressDict[address]

    return sum
def computeValue2(address, mask, value, addressDict):
    addressBin = value2bin(int(address), len(mask))
    result = addressBin
    floatIdx = []
    for i in range(len(mask)):
        if mask[i] == 'X':
            result[i] = 'X'
            floatIdx.append(i)
        elif mask[i] == '1':
            result[i] = '1'

    for i in range(2**len(floatIdx)):
        rep = str(bin(i))[2:]
        realrep = ['0'] * len(floatIdx)
        startIdx = len(floatIdx) - len(rep)
        for i in range(startIdx,len(floatIdx)):
            realrep[i] = rep[i-startIdx]
        tmpResult = [x for x in result]
        for i in range(len(floatIdx)):
            tmpResult[floatIdx[i]] = realrep[i]
        rv = ''.join(tmpResult)
        addressDict[bin2value(rv)] = value

def day14P2(instructions):
    mask = ""
    addressDict = dict()
    for ins in instructions:
        if "mask" in ins:
            mask = ins.split(" ")[2]
        elif "mem" in ins:
            b = [x.strip(" ") for x in ins.split("=")]
            address = b[0][4:-1]
            value = int(b[1])
            computeValue2(address, mask, value, addressDict)
    sum = 0
    for address in addressDict:
        sum += addressDict[address]

    return sum

if __name__ == "__main__":
    ins = readFile("./input")
    #value = day14P1(ins)
    value = day14P2(ins)

    print(value)
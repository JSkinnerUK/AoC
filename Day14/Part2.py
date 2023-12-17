import re
from functools import cache

with open('Day14/input.txt', 'r') as file:
    data = tuple(tuple(line.strip()) for line in file)

@cache
def getBoulderPaths(line):
    return ((m.start(0), m.end(0)) for m in re.finditer(r'[O.]+', ''.join(line)))

@cache
def sortPath(path):
    countBoulder = path.count('O')
    countEmpty = path.count('.')
    return ['O'] * countBoulder + ['.'] * countEmpty 

@cache 
def sortLine(line, paths):
    temp = list(line)
    for path in paths:
        temp[path[0]:path[1]] = sortPath(line[path[0]:path[1]])
    return tuple(temp)

@cache
def performTilt(data):
    temp = list(data)
    for i, line in enumerate(data):
        paths = getBoulderPaths(line)
        temp[i] = sortLine(line, paths)
    return tuple(temp)

@cache
def transpose(data):
    return tuple(zip(*data))

@cache
def reverse_rows(data):
    return tuple(row[::-1] for row in data)


def cycleUp(data):
    data = transpose(data)
    data = performTilt(data)
    return data

def cycleLeft(data):
    data = transpose(data)
    data = performTilt(data)
    return data

def cycleDown(data):
    data = transpose(data)
    data = reverse_rows(data)
    data = performTilt(data)
    data = reverse_rows(data)
    data = transpose(data)
    return data

def cycleRight(data):
    data = reverse_rows(data)
    data = performTilt(data)
    data = reverse_rows(data)
    return data

@cache
def getCycle(data):
    data = cycleUp(data)
    data = cycleLeft(data)
    data = cycleDown(data)
    data = cycleRight(data)
    return data

def getLoad(data):
    total = 0
    dataLen = len(list(data))
    for i, line in enumerate(data):
        total += line.count('O') * (dataLen - i)
    return total

loopSize = loopStart = 0

visted = dict()
for i in range(1000000000):
    visted[data] = i
    data = getCycle(data)
    if data in visted:
        loopSize = i - visted[data] + 1
        loopStart = visted[data] + 1
        break
print(loopSize, loopStart)
for i in range(loopSize - loopStart):
    data = getCycle(data)

print(getLoad(data))

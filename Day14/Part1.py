import re
from functools import cache

with open('Day14/input.txt', 'r') as file:
    data = [line.strip() for line in file]

@cache
def getBoulderPaths(line):
    return [(m.start(0), m.end(0)) for m in re.finditer(r'[O.]+', line)]

@cache
def sortPath(path):
    countBoulder = path.count('O')
    countEmpty = path.count('.')
    return 'O' * countBoulder + '.' * countEmpty

# Loop through columns in data
for i in range(len(data[0])):
    column = ''.join([line[i] for line in data])
    paths = getBoulderPaths(column)
    for path in paths:
        column = column[:path[0]] + sortPath(column[path[0]:path[1]]) + column[path[1]:]
    print(column)
    for j, line in enumerate(data):
        data[j] = data[j][:i] + column[j] + data[j][i+1:]


def getLoad(data):
    total = 0
    dataLen = len(data)
    for i, line in enumerate(data):
        total += line.count('O') * (dataLen - i)
    return total

print(getLoad(data))

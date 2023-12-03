import re

total = 0

def getSymbols(data):
    symbols = set()
    ignore = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'}
    for line in data:
        symbols.update(list(line))
        symbols = symbols.difference(ignore)

    return symbols

def getNums(line):
    matches = re.finditer('[0-9]+', line)
    numbers = [(m.start(0), m.end(0), m.group()) for m in matches]
    return numbers

def checkContains(line, start, end, symbols):
    subString = line[max(start-1, 0):min(end+1, len(line))]
    return set(list(subString)).intersection(symbols)


with open('Day03/input.txt', 'r') as file:
    #Ignore the \n on each line
    data = [line[:-1] for line in file]

symbols = getSymbols(data)

for i, line in enumerate(data):
    nums = getNums(line)
    for num in nums:
        for j in range(-1,2):
            if (i+j >= 0 and i+j < len(data)):
                if checkContains(data[i+j], num[0], num[1], symbols):
                    total += int(num[2])
                    break

print(total)            

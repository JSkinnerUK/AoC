import re
import math

with open('Day08/input.txt', 'r') as file:
    data = [line[:-1] for line in file]


instructions = list(data[0])
network = data[2:]

networkDict = {x: (y, z) for n in network for x, y, z in [re.findall(r'\w+', n)]}

start = [x for x in networkDict.keys() if x[-1] == 'A']
finish = [x for x in networkDict.keys() if x[-1] == 'Z']

def findFinishes(startPos): 
    position = startPos
    checked = set()
    endPosition = 0
    count = 1
    while True:
        for i, instruction in enumerate(instructions):
            x = networkDict.get(position)

            if x:
                if instruction == 'L':
                    position = x[0]
                else:
                    position = x[1]

            if (i, position) in checked:
                return endPosition
            checked.add((i, position))
            if position[-1] == 'Z':
                endPosition = count
            count+=1

result = 1
for position in start:
    result = math.lcm(result, findFinishes(position))
print(result)

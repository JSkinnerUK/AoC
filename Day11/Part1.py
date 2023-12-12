import re
from itertools import combinations

with open('Day11/input.txt', 'r') as file:
    data = [line.strip() for line in file]

noGalaxies = ([],[])

def galaxy(match, lineNum):
    galaxy.counter += 1
    galaxy.locations.append((lineNum, match.start()))
    return str(galaxy.counter)

galaxy.counter = 0
galaxy.locations = []


for i in range(len(data)):
    if len(set(data[i])) == 1:
        noGalaxies[0].append(i)
for j in range(len(data[0])):
    if len(set([item[j] for item in data])) == 1:
        noGalaxies[1].append(j)

def expandUniverse(data, noGalaxies):
    for m, i in enumerate(noGalaxies[0]):
        data.insert(i+m, '.' * len(data[0]))
    for l, j in enumerate(noGalaxies[1]):
        for k in range(len(data)):
            data[k] = data[k][:j+l] + '.' + data[k][j+l:]

def manhattanDistance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

expandUniverse(data, noGalaxies)

for i, line in enumerate(data):
    data[i] = re.sub(r"#", lambda match: galaxy(match, i), line) 

combos = combinations(galaxy.locations, 2)

pathDistance = 0
for combo in combos:
    pathDistance += manhattanDistance(combo[0], combo[1])

print(pathDistance)

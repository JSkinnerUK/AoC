import numpy as np

with open('Day05/test.txt', 'r') as file:
    data = [line for line in file]

seedRange = data[0][data[0].find(':')+1:].strip().split(' ')
seeds = []

for i in range(0, len(seedRange), 2):
    start = int(seedRange[i])
    rnge = int(seedRange[i+1])
    seeds.append((start, rnge))

seedMax = max([start+rnge-1 for start, rnge in seeds])
seedArr = np.full(seedMax+1, np.inf)

for seed in seeds:
    seedArr[seed[0]:seed[0]+seed[1]] = np.arange(seed[0],seed[0]+seed[1])


mapsIndex = [i for i, s in enumerate(data) if "map" in s]

for index in mapsIndex:
    index += 1
    while index < len(data) and data[index] != '\n':
        destination, source, rangeLen = [int(x) for x in data[index][:-1].split(' ')]
        index += 1
        seedArr[source:source+rangeLen] += destination - source
print(min(seedArr))

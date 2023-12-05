with open('Day05/input.txt', 'r') as file:
    data = [line for line in file]

seeds = data[0][data[0].find(':')+1:].strip().split(' ')
mapsIndex = [i for i, s in enumerate(data) if "map" in s]
locations = []

for seed in seeds:
    val = int(seed)
    for index in mapsIndex:
        index += 1
        while index < len(data) and data[index] != '\n':
            destination, source, rangeLen = [int(x) for x in data[index][:-1].split(' ')]
            if val >= source and val <= source + rangeLen:
                val = destination + (val - source)
                break;
            index += 1
    locations.append(val)

print(min(locations))

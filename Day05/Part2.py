with open('Day05/input.txt', 'r') as file:
    data = [line for line in file]

seedRange = data[0][data[0].find(':')+1:].strip().split(' ')
seeds = [(int(seedRange[i]), int(seedRange[i+1])) for i in range(0, len(seedRange), 2)]

mapsIndex = [i for i, s in enumerate(data) if "map" in s]
maps = [[] for _ in range(len(mapsIndex))]

for i, map in enumerate(mapsIndex):
    for line in data[map+1:]:
        if line == '\n':
            break
        maps[i].append([int(x) for x in line[:-1].split(' ')])

def applyToSeedRange(start, end, transform, transformStart, transformEnd):
    unchanged = []
    changed = []

    overlapStart = max(start, transformStart)
    overlapEnd = min(end, transformEnd)
    if overlapStart < overlapEnd:
        if start < overlapStart:
            unchanged.append((start, overlapStart-start))
        changed.append((overlapStart+transform, overlapEnd - overlapStart))
        if end > overlapEnd:
            unchanged.append((overlapEnd, end - overlapEnd))
    else:
        unchanged.append((start, end - start))

    return unchanged, changed

def applyTransform(seeds, transform):
    unchanged = []
    changed = []
    transform, transformStart, transformEnd = -(transform[1]-transform[0]), transform[1], transform[1] + transform[2]
    for seed in seeds:
        seedStart, seedEnd = seed[0], seed[0] + seed[1]
        x,y = applyToSeedRange(seedStart, seedEnd, transform, transformStart, transformEnd)
        unchanged.extend(x)
        changed.extend(y)
    return unchanged, changed

for map in maps:
    x = []
    for transform in map:
        p, v = applyTransform(seeds, transform)
        seeds = p
        x.extend(v)
    seeds.extend(x)


first_element = lambda x: x[0]
print(min(seeds, key=first_element)[0])

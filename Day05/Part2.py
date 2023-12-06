import re

with open('Day05/input.txt', 'r') as file:
    data = [line for line in file]

seedRange = data[0][data[0].find(':')+1:].strip().split(' ')
seeds = [(int(seedRange[i]), int(seedRange[i+1])) for i in range(0, len(seedRange), 2)]

mapsIndex = [(match.group(1), i) for i, s in enumerate(data) if "map" in s and (match := re.search(r'to-(\w+)\smap', s))]
maps = [(map[0], []) for map in mapsIndex]

for i, map in enumerate(mapsIndex):
    for line in data[map[1]+1:]:
        if line == '\n':
            break
        maps[i][1].append([int(x) for x in line[:-1].split(' ')])

# print("Seeds:", seeds)
# print('Maps:', maps)

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
        print("CHANGED")
    else:
        print("No change")
        unchanged.append((start, end - start))

    print("Changed:", changed)
    print("Unchanged:", unchanged)
    return unchanged, changed

def applyTransform(seeds, transform):
    unchanged = []
    changed = []
    print("Appling transform:", transform, "to seeds:", seeds)
    transform, transformStart, transformEnd = -(transform[1]-transform[0]), transform[1], transform[1] + transform[2]
    for seed in seeds:
        seedStart, seedEnd = seed[0], seed[0] + seed[1]
        print("Seed:", seedStart, seedEnd)
        x,y = applyToSeedRange(seedStart, seedEnd, transform, transformStart, transformEnd)
        unchanged.extend(x)
        changed.extend(y)
    print("Transform:", transform, transformStart, transformEnd)
    return unchanged, changed

for mapName, map in maps:
    print('-'*50)
    print("Map:", mapName, map)
    x = []
    for transform in map:
        p, v = applyTransform(seeds, transform)
        seeds = p
        x.extend(v)
    seeds.extend(x)
    print(seeds)


first_element = lambda x: x[0]
print(min(seeds, key=first_element)[0])

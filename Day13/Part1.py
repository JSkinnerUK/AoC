from functools import cache

with open('Day13/input.txt', 'r') as file:
    split = file.read().strip().split('\n\n')
    patterns = [[tuple(line) for line in pattern.split('\n')] for pattern in split] 

@cache
def checkMirrored(before, after):
    return before == after[::-1]

@cache
def findCandidates(line):
    candidates = set()
    for i in range(1, len(line)):
        before, after = line[:i], line[i:]
        checking = min(len(before), len(after))
        if checkMirrored(before[-checking:], after[:checking]):
            candidates.add(i)
    return candidates

total = 0

for i, pattern in enumerate(patterns):
    width, height = len(pattern[0]), len(pattern)
    validVert = set(range(1, width))
    validHor = set(range(1, height))
    for line in pattern:
        validVert = validVert.intersection(findCandidates(line))
        if validVert == set():
            break

    for i in range(width):
        column = tuple(line[i] for line in pattern)
        validHor = validHor.intersection(findCandidates(column))
        if validHor == set():
            break

    total += sum(validVert) + sum(validHor) * 100

print(total)

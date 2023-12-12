import re
from itertools import product

with open('Day12/input.txt', 'r') as file:
    data = [line.strip() for line in file]

def validateLine(input, validation):
    blocks = re.findall(r'[#]+', input)
    if len(blocks) != len(validation):
        return False
    for i, j in zip(blocks, validation):
        if len(i) != int(j):
            return False
    return True

def checkPermutations(input, validation, unknowns):
    permutations = []
    for combination in product(['#', '.'], repeat=unknowns):
        temp = input
        for char in combination:
            temp = re.sub(r'\?', char, temp, count=1)
        if validateLine(temp, validation):
            permutations.append(temp)
    return permutations

total = 0

for line in data:
    input, validation = line.split(' ')
    validation = validation.split(',')

    unknowns = input.count('?')

    total += len(checkPermutations(input, validation, unknowns))

print(total)

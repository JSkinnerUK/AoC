import re

total = 0

with open('Day09/input.txt', 'r') as file:
    data = [[int(x) for x in re.findall(r'-?\d+', line[:-1])] for line in file]

def findSequence(arr):
    if set(arr) == {0}:
        return 0

    steps = []
    for char in range(len(arr) -1):
        steps.append(arr[char+1] - arr[char])
    return arr[0] - findSequence(steps)

for line in data:
    total += findSequence(line)

print(total)

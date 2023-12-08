import re

with open('Day08/input.txt', 'r') as file:
    data = [line[:-1] for line in file]


instructions = list(data[0])
network = data[2:]

a = {x: (y, z) for n in network for x, y, z in [re.findall(r'\w+', n)]}

count = 0
found = False
current = 'AAA'
while not found:
    for instruction in instructions:
        # print(instruction)
        x = a.get(current)
        if not x: break

        if instruction == 'L':
            current = x[0]
        else:
            current = x[1]
        count+=1
        print(current)
        if current == 'ZZZ': found = True

print(count)


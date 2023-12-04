import re

with open('Day04/input.txt', 'r') as file:
    data = [line for line in file]

total = {i+1:1 for i in range(len(data))}

for i, line in enumerate(data, 1):
    expr = r'(\d+)'
    winningNums = re.findall(expr, line[line.find(':')+1:line.find('|')])
    elfNums = re.findall(expr, line[line.find('|')+1:])


    intersect = set(winningNums).intersection(set(elfNums))
    count = len(intersect)

    for card in range(total[i]):
        for j in range(count):
            total[i+j+1] += 1

print(sum(total.values()))

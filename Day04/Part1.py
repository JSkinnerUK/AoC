import re

total = 0

with open('Day04/input.txt', 'r') as file:
    for line in file:
        expr = r'(\d+)'
        winningNums = re.findall(expr, line[line.find(':')+1:line.find('|')])
        elfNums = re.findall(expr, line[line.find('|')+1:])


        intersect = set(winningNums).intersection(set(elfNums))
        count = len(intersect)

        if count > 0:
            total += 2 ** (count-1)

print(total)

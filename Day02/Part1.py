import re

total = 0
criteria = (12, 13, 14)

with open('Day02/input.txt', 'r') as file:
    for line in file:
        failed = False
        gameId = int(re.findall(r'Game\s(\d+)', line)[0])
        red = max(list(map(int, re.findall(r'(\d+)\sred', line))))
        green = max(list(map(int, re.findall(r'(\d+)\sgreen', line))))
        blue = max(list(map(int,re.findall(r'(\d+)\sblue', line))))
        for l1, l2 in zip(criteria, (red, green, blue)):
            if l1 < int(l2):
                failed = True
                break
        if (failed == False): total+=gameId


print(total)


import re

total = 0
criteria = (12, 13, 14)

with open('Day02/input.txt', 'r') as file:
    for line in file:
        gameId = int(re.findall(r'Game\s(\d+)', line)[0])
        match = re.findall(r'(\d+)\s(red|green|blue)', line)
        red, green, blue = (max(int(num) for num, color in match if color == c) 
                for c in ['red', 'green', 'blue'])
        
        total += red * green * blue

print(total)

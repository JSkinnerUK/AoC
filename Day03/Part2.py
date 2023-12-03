import re

total = 0

def getStars(line):
    return [(m.start(0)) for m in re.finditer(r'\*', line)]

def getNums(line):
    matches = re.finditer('[0-9]+', line)
    numbers = [(m.start(0), m.end(0), m.group()) for m in matches]
    return numbers

def checkContains(starPos, start, end):
    return starPos <= end and starPos >= start-1 


with open('Day03/input.txt', 'r') as file:
    #Ignore the \n on each line
    data = [line[:-1] for line in file]

for i, line in enumerate(data):
    stars = getStars(line)
    for star in stars:
        adjacent = 0
        mult = 1
        for j in range(-1,2):
            if (i+j >= 0 and i+j < len(data)):
                nums = getNums(data[i+j]);
                for num in nums:
                    if checkContains(star, num[0], num[1]):
                        adjacent += 1
                        mult *= int(num[2])
        if adjacent == 2:
            total += mult

print(total)            

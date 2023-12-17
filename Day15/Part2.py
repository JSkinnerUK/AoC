import re

with open('Day15/input.txt', 'r') as file:
    data = [line.strip().split(',') for line in file][0]

boxes = {i: [] for i in range(255)}

def calcHash(string):
    hash = 0
    prev = 0
    for char in string:
        prev = ((ord(char) + prev) * 17) % 256
        hash = prev
    return hash

for step in data:
    match = re.match(r'([a-zA-Z]+)([-=])(\d*)', step)
    if match:
        label, operation, value = match.groups()
        box = calcHash(label)
        if operation == '-':
             boxes[box] = [i for i in boxes[box] if i and i[0] != label]
        elif operation == '=':
            found = False
            for i, item in enumerate(boxes[box]):
                if item and item[0] == label:
                    found = True
                    boxes[box][i] = (label, int(value))
                    break 
            if not found:
                boxes[box].append((label, int(value)))
            
total = 0
for i, box in enumerate(boxes.values()):
    for j, (_, value) in enumerate(box):
        total += (i+1) * (j+1) * value

print(total)

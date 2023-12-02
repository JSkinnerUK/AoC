total = 0

with open('Day01/input.txt', 'r') as file:
    for line in file:
        digits = ''.join(c for c in line if c.isdigit())
        total += int(digits[0]+digits[-1])

print(total)

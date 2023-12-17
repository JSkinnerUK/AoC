with open('Day15/test.txt', 'r') as file:
    data = [line.strip().split(',') for line in file][0]
    print(data)

def calcHash(string):
    hash = 0
    prev = 0
    for char in string:
        prev = ((ord(char) + prev) * 17) % 256
        hash = prev
    return hash

total = 0
for step in data:
    total += calcHash(step)

print(total)

pos = (0, 0)
data = []
path = []
prev = 0b0000
mask = 0b1111
total = 0

pipes = {
    # North, East, South, West
    '|': 0b1010,
    '-': 0b0101,
    'L': 0b1100, 
    'J': 0b1001,
    '7': 0b0011,
    'F': 0b0110,
}

neighbours = {
    0b1000: (0, -1),
    0b0100: (1, 0),
    0b0010: (0, 1),
    0b0001: (-1, 0),
}

with open('Day10/input.txt', 'r') as file:
    for i, line in enumerate(file):
        data.append(line.strip())
        if 'S' in line:
            pos = (line.index('S'), i)

def getOpposite(direction):
    x = 0b0000
    if direction == 0b1000:
        x = 0b0010
    elif direction == 0b0100:
        x = 0b0001
    elif direction == 0b0010:
        x = 0b1000
    elif direction == 0b0001:
        x = 0b0100
    return x

def getValidMove(pos):
    for direction, adjustment in neighbours.items():
        if pos[0] + adjustment[0] < 0 or pos[0] + adjustment[0] >= len(data[0]):
            continue 
        if pos[1] + adjustment[1] < 0 or pos[1] + adjustment[1] >= len(data):
            continue

        newPos = (pos[0] + adjustment[0], pos[1] + adjustment[1])
        symbol = data[newPos[1]][newPos[0]]
        if symbol not in pipes:
            continue
        x = getOpposite(direction)

        if pipes[symbol] & x != 0:
            return newPos, x
    return (0,0), 0

def getNext(pos, prev):
    symbol = data[pos[1]][pos[0]]
    if symbol == 'S':
        return getValidMove(pos)

    move = pipes[symbol] ^ prev
    neighboursAdjustment = neighbours[move]
    newPos = (pos[0] + neighboursAdjustment[0], pos[1] + neighboursAdjustment[1])
    return newPos, getOpposite(move)

while pos not in path:    
    path.append(pos)
    pos, prev = getNext(pos, prev)

path.append(path[0])

for i in range(len(path) - 1):
    total += path[i][1] * path[i + 1][0] - path[i][0] * path[i + 1][1]
area = abs(total/2)
contained = area - (len(path)-1)/2 + 1
print(int(contained))

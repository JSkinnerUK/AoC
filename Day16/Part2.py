import enum

with open('Day16/input.txt', 'r') as file:
    data = [list(line.strip()) for line in file]

class Direction(enum.Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

def move(position, direction):
    if direction == Direction.UP:
        return (position[0], position[1] - 1)
    if direction == Direction.RIGHT:
        return (position[0] + 1, position[1])
    if direction == Direction.DOWN:
        return (position[0], position[1] + 1)
    if direction == Direction.LEFT:
        return (position[0] - 1, position[1])

def isValidPosition(position):
    if position[0] < 0 or position[0] >= len(data[0]):
        return False
    if position[1] < 0 or position[1] >= len(data):
        return False
    return True

def forwardTransform(direction):
    if direction == Direction.UP:
        return Direction.RIGHT
    if direction == Direction.RIGHT:
        return Direction.UP
    if direction == Direction.DOWN:
        return Direction.LEFT
    if direction == Direction.LEFT:
        return Direction.DOWN


def backwardTransform(direction):
    return Direction(3 - direction.value)

def getEnergised(start):
    beams = []
    temp = start
    p = set()
    while True:
        beams = temp
        before = len(p)
        p = p.union({i for i in temp})
        temp = []
        if before == len(p):
            break

        for i, beam in enumerate(beams):
            position = (beam[0], beam[1])
            beamDirection = Direction(beam[2])

            newPos = move(position, beamDirection)

            if not newPos or not isValidPosition(newPos):
                continue

            symbol = data[newPos[1]][newPos[0]]

            tmp2 = []
            if symbol == '.':
                tmp2 = [(newPos[0], newPos[1], beamDirection)]
            elif symbol == '/' :
                tmp2 = [(newPos[0], newPos[1], forwardTransform(beamDirection))]
            elif symbol == '\\':
                tmp2 = [(newPos[0], newPos[1], backwardTransform(beamDirection))]
            elif symbol == '-':
                if beamDirection == Direction.UP or beamDirection == Direction.DOWN:
                    tmp2 = [(newPos[0], newPos[1], Direction.LEFT), (newPos[0], newPos[1], Direction.RIGHT)]
                else:
                    tmp2 = [(newPos[0], newPos[1], beamDirection)]
            elif symbol == '|':
                if beamDirection == Direction.LEFT or beamDirection == Direction.RIGHT:
                    tmp2 = [(newPos[0], newPos[1], Direction.UP), (newPos[0], newPos[1], Direction.DOWN)]
                else:
                    tmp2 = [(newPos[0], newPos[1], beamDirection)]

            for i in tmp2:
                if i not in p:
                    temp.append(i)

    q = {(r[0], r[1]) for r in p}
    return len(q) - 1

getEnergised([(-1,0,Direction.RIGHT)])

mx = 0
for i in range(len(data)):
    a = getEnergised([(-1,i,Direction.RIGHT)])
    mx = max(mx, a)
for i in range(len(data)):
    a = getEnergised([(len(data[0])+1,i,Direction.LEFT)])
    mx = max(mx, a)
for i in range(len(data[0])):
    a = getEnergised([(i,-1,Direction.DOWN)])
    mx = max(mx, a)
for i in range(len(data[0])):
    a = getEnergised([(i,len(data)+1,Direction.DOWN)])
    mx = max(mx, a)
print(mx)


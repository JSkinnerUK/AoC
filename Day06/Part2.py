import re
import math

total = 1

with open('Day06/input.txt', 'r') as file:
    data = [line for line in file]

time = int(''.join(re.findall(r'\d+', data[0])))
distance = int(''.join(re.findall(r'\d+', data[1])))

def quadFormula(a, b, c):
    plus = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    minus = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return (plus, minus)

def custom_ceil(x):
    if x == int(x):
        return int(x) +1
    return math.ceil(x)

def custom_floor(x):
    if x == int(x):
        return int(x) -1
    return math.floor(x)


x, y = quadFormula(-1, time, -distance)

total *= custom_floor(y)-custom_ceil(x)+1
print(total)

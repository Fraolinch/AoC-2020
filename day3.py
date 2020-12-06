with open("input3", 'r') as file:
    lines = file.read().splitlines()

width = len(lines[0])
height = len(lines)
x = 0
y = 0
trees = 0

while y < height:
    if lines[y][x] == '#':
        trees = trees + 1
    x = (x + 3) % width
    y = y + 1

print(trees)
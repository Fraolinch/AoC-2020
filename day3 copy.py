with open("input3", 'r') as file:
    lines = file.read().splitlines()

def seek_trees(track, offsetx, offsety):

    width = len(track[0])
    height = len(track)
    x = 0
    y = 0
    trees = 0

    while y < height:
        if lines[y][x] == '#':
            trees = trees + 1
        x = (x + offsetx) % width
        y = y + offsety
    return trees

print((seek_trees(lines, 1, 1)) *
(seek_trees(lines, 3, 1)) *
(seek_trees(lines, 5, 1)) *
(seek_trees(lines, 7, 1)) *
(seek_trees(lines, 1, 2)))
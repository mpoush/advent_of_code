def dist(x, y):
    return (abs(x) + abs(y))/2

def steps_in(pathString):
    largest_distance = 0
    path = pathString.split(",")
    x = 0
    y = 0
    for p in path:
        dx = 0
        dy = 2
        if p[0] == 's':
            dy = -2
        if len(p) == 2:
            dy /= 2
            if p[1] == 'e':
                dx = 1
            else:
                dx = -1
        x += dx
        y += dy
        largest_distance = max(largest_distance, dist(x, y))
    return dist(x, y), largest_distance

assert steps_in("ne,ne,ne") == (3, 3)
assert steps_in("ne,ne,sw,sw") == (0, 2)
assert steps_in("ne,ne,s,s") == (2, 2)
assert steps_in("se,sw,se,sw,sw") == (3, 3)

with open("day11.txt") as f:
    data = ''.join(f.readlines()).strip()
    print steps_in(data)

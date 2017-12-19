def in_grid(x, y, grid):
    if 0 <= y < len(grid):
        if 0 <= x < len(grid[y]):
            if grid[y][x] != ' ':
                return True
    return False

def next_direction(last_pos, x, y, grid):
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        x1 = dx + x
        y1 = dy + y
        if (x1, y1) == last_pos:
            continue
        if in_grid(x1, y1, grid):
            return dx, dy
    return None

def run(grid):
    x, y = grid[0].index('|'), 0
    dx, dy = 0, 1
    last_pos = -1, -1
    ix = 0
    seen = []
    while True:
        ix += 1
        char = grid[y][x]
        if char not in '|-+':
            seen.append(char)
        if not in_grid(x+dx, y+dy, grid):
            n = next_direction(last_pos, x, y, grid)
            if n is None:
                return ''.join(seen), ix
            dx, dy = n
        last_grid = x, y
        y += dy
        x += dx

sample = [
"     |          ",
"     |  +--+    ",
"     A  |  C    ",
" F---|----E|--+ ",
"     |  |  |  D ",
"     +B-+  +--+ "
]

assert run(sample) == ('ABCDEF', 38)

with open('day19.txt') as f:
    data = f.readlines()
print run(data)

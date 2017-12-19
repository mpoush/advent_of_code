from collections import defaultdict

def size_of_group_containing(n, remain, connections):
    seen = set([])
    to_evaluate = [n]
    while to_evaluate:
        current = to_evaluate.pop()
        if current in seen:
            continue
        remain.remove(current)
        seen.add(current)
        for t in connections[current]:
            if t not in seen:
                to_evaluate.append(t)
    return len(seen)

def group_sizes(connections):
    remain = set(connections.keys())
    while remain:
        candidate = next(x for x in sorted(remain))
        yield size_of_group_containing(candidate, remain, connections)

def analyze(dataString):
    connections = defaultdict(set)
    for line in dataString:
        [f, _, toListString] = line.split(" ", 2)
        for t in toListString.split(", "):
            connections[f].add(t)
            connections[t].add(f)
    return connections

def solve(dataString):
    connections = analyze(dataString)
    sizes = list(group_sizes(connections))
    return sizes[0], len(sizes)

sample = [
    "0 <-> 2",
    "1 <-> 1",
    "2 <-> 0, 3, 4",
    "3 <-> 2, 4",
    "4 <-> 2, 3, 6",
    "5 <-> 6",
    "6 <-> 4, 5"
]
assert solve(sample) == (6, 2)

with open("day12.txt") as f:
    data = map(str.strip, f.readlines())
    print solve(data)

def ints(r):
    return map(int, r.split())

def checksum_row(r):
    ns = ints(r)
    return max(ns) - min(ns)

def do_division(r):
    ns = sorted(ints(r))
    for a in xrange(len(ns)):
        for b in xrange(a+1, len(ns)):
            if ns[b] % ns[a] == 0:
                return ns[b] / ns[a]

lines = ["5 1 9 5", "7 5 3", "2 4 6 8"]
assert sum(map(checksum_row, lines)) == 18

with open("day2.txt") as f:
    lines = map(str.strip, f.readlines())

print sum(map(checksum_row, lines))
print sum(map(do_division, lines))

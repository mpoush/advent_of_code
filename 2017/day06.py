def reorder(ls):
    val = max(ls)
    ix = ls.index(val)
    ls[ix] = 0
    for i in xrange(ix + 1, ix + val + 1):
        ls[i % len(ls)] += 1
    return tuple(ls)

def run(banks):
    for _ in xrange(2):
        seen = set([banks])
        while True:
            banks = reorder(list(banks))
            if banks in seen:
                yield len(seen)
                break
            seen.add(banks)

banks = tuple([0, 2, 7, 0])

assert list(run(banks)) == [5, 4]

banks = tuple([4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5])

print list(run(banks))

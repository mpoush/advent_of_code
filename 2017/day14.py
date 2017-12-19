from itertools import chain
from day10 import knot_hash

def count_regions(values):
    def neighbors(x, y):
        yield x+1, y
        yield x, y+1
        yield x-1, y
        yield x, y-1

    existing = set(values)
    sets = 0
    while(existing):
        in_current = [existing.pop()]
        while in_current:
            current = in_current.pop()
            for n in neighbors(*current):
                if n not in existing:
                    continue
                in_current.append(n)
                existing.remove(n)
        sets += 1
    return sets

def bits_on_in(hash_string):
    chunks = map(bits, knot_hash(hash_string))
    for x, r in enumerate(chain.from_iterable(chunks)):
        if r == '1':
            yield x

def get_bits_on(hash_string):
    for y in xrange(128):
        for x in bits_on_in("%s-%s" % (hash_string, y)):
            yield x, y

def count_bits_on(hash_string):
    return sum(1 for _ in get_bits_on(hash_string))

def bits(n):
    return bin(int(n, 16))[2:].zfill(4)

if __name__ == '__main__':
    assert count_bits_on("flqrgnkx") == 8108
    assert count_regions(get_bits_on("flqrgnkx")) == 1242

    print count_bits_on("ffayrhll")
    print count_regions(get_bits_on("ffayrhll"))

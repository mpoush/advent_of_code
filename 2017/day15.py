def generate(start, factor, mod):
    while True:
        start *= factor
        start %= 2147483647
        if not start & mod:
            yield start & 65535

def count_pairs(runs, start_a, start_b, skip=False):
    a = generate(start_a, 16807, 3 if skip else 0)
    b = generate(start_b, 48271, 7 if skip else 0)
    return sum(next(a) == next(b) for _ in xrange(runs))

if __name__ == '__main__':
    assert count_pairs(40000000, 65, 8921) == 588
    assert count_pairs(5000000, 65, 8921, True) == 309
    print count_pairs(40000000, 516, 190)
    print count_pairs(5000000, 516, 190, True)

from hashlib import md5


def get_smallest(txt, needed='00000', start=0):
    range = xrange(start+1, 999999999999)
    for x in range:
        r = md5(txt + str(x))
        digest = r.hexdigest()
        if digest.startswith(needed):
            return x, digest[5], digest[6]


def get_digits(code):
    return ''.join(list(yield_digits(code)))


def yield_digits(code):
    start = 0
    for _ in xrange(8):
        start, n, _ = get_smallest(code, start=start)
        print n
        yield n


def get_digits_harder(code):
    chars = [None for _ in xrange(8)]
    start = 0
    while True:
        start, p, n = get_smallest(code, start=start)
        if p not in "01234567":
            continue
        p = int(p)
        if chars[p] is None:
            chars[p] = n
            if None not in chars:
                return as_string(chars)
            print as_string(chars)


def as_string(chars):
    return ''.join(map(lambda t: t if type(t) is str else '.', chars))


if __name__ == '__main__':
    puzzle_input = "ugkcyxxp"
    print get_digits(puzzle_input) == "d4cd2ee1"
    print get_digits_harder(puzzle_input) == "f2c730e5"

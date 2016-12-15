from hashlib import md5
from itertools import count


def yield_each_hash(salt, use_stretching):
    to_repeat = 2017 if use_stretching else 1
    for current in count():
        key = salt + str(current)
        for _ in xrange(to_repeat):
            key = md5(key).hexdigest().lower()
        yield key


def yield_hashes(salt, use_stretching):
    r = yield_each_hash(salt, use_stretching)
    ls = [next(r) for _ in xrange(1001)]
    while True:
        next_digest = next(r)
        n = ls[1:]
        yield ls[0], n
        ls = n
        ls.append(next_digest)


def find_three(s):
    while len(s) > 2:
        if s[0] == s[1] and s[1] == s[2]:
            return s[0]
        s = s[1:]
    return None


def exists(needle, haystack):
    return any(needle in hay for hay in haystack)


def f(salt, use_stretching=False):
    remaining = 64
    for ix, (current, next_thousand) in enumerate(yield_hashes(salt, use_stretching)):
        c = find_three(current)
        if c is None:
            continue
        needle = c * 5
        if exists(needle, next_thousand):
            print remaining, ix
            remaining -= 1
            if not remaining:
                return ix


if __name__ == '__main__':
    print f('jlmsuwbz') == 35186
    print f('jlmsuwbz', True)

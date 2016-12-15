import helpers
from itertools import count


def to_discs(line):
    words = line.split(' ')
    return int(words[3]), int(words[-1][:-1])


def time_to_hit(lines):
    discs = map(to_discs, lines)
    n = len(discs)
    for i in count():
        if not any((i + ix + discs[ix][1]) % discs[ix][0] for ix in xrange(n)):
            return i - 1


if __name__ == '__main__':
    sample_lines = """
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
""".strip().splitlines()

    helpers.verify(5, time_to_hit, sample_lines)

    real_lines = helpers.get_all_lines('day15_input.txt')
    helpers.verify(122318, time_to_hit, real_lines[:-1])

    helpers.verify(3208583, time_to_hit, real_lines)

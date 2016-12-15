import helpers


def is_valid(points):
    p = sorted(points)
    return p[0] + p[1] > p[2]


def to_points(line):
    return map(int, [p for p in map(str.strip, line.split(' ')) if p])


def count_triangles(lines):
    return sum(map(is_valid, lines))


def rotate(lines):
    iterator = iter(lines)
    for line in iterator:
        [a, d, g] = line
        [b, e, h] = next(iterator)
        [c, f, i] = next(iterator)
        yield [a, b, c]
        yield [d, e, f]
        yield [g, h, i]


def count_triangles_by_cols(lines):
    return count_triangles(rotate(lines))


if __name__ == '__main__':
    data = map(to_points, helpers.get_all_lines('day3_input.txt'))
    print count_triangles(data), 869
    print count_triangles_by_cols(data), 1544

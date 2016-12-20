def tuples(ls):
    yield 1, ls[0], ls[1]
    while len(ls) > 2:
        yield ls[0], ls[1], ls[2]
        ls = ls[1:]
    yield ls[0], ls[1], 1

traps = {(0, 0, 1), (1, 0, 0), (1, 1, 0), (0, 1, 1)}
def is_safe(tup):
    return tup not in traps

memo = {}

def next_row(row):
    if row in memo:
        return memo[row]
    answer = tuple(map(is_safe, tuples(row)))
    memo[row] = answer
    return answer

def f(pattern_string, rows):
    ls = tuple([x == '.' for x in pattern_string])
    answer = sum(ls)
    for ix in xrange(rows-1):
        ls = next_row(ls)
        answer += sum(ls)
        print rows - ix
        # print ls
    return answer
    # return ls

if __name__ == '__main__':
    print f('..^^.', 3) == 6
    print f('.^^.^.^^^^', 10) == 38
    input = '.^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^.'
    print f(input, 40)
    print f(input, 400000)

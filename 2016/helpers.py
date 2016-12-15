def verify(known, method, *args):
    actual = method(*args)
    if actual != known:
        string_args = ', '.join(map(repr, args))
        method_name = method.func_name
        print ''
        print 'Error! %s(%s):' % (method_name, string_args)
        print '\tExpected:', known
        print '\t but was:', actual


def move((x, y), (dx, dy)):
    return x+dx, y+dy


def get_all_lines(filename):
    with open(filename) as f:
        return [x.strip() for x in f.readlines()]


def get_first_line(filename):
    return get_all_lines(filename)[0]


def print_all(ls):
    for ix, row in enumerate(ls):
        print ix, row


def print_dictionary(d):
    for k in sorted(d.keys()):
        print '\t',k, d[k]

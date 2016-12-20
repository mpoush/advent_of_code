import helpers


def get_ranges(ls):
    current_start, current_end = 0, 0
    for start, end in sorted(map(int, x.split('-')) for x in ls):
        if start - 1 > current_end:
            yield current_start, current_end
            current_start, current_end = start, end
            continue
        if start < current_start:
            current_start = start
        if end > current_end:
            current_end = end
    yield current_start, current_end


def get_leftovers(ls):
    for start, end in get_ranges(ls):
        if end == 4294967295:
            return
        yield end+1

lines = helpers.get_all_lines('day20_input.txt')

test = list(get_leftovers(lines))
print test[0], len(test)

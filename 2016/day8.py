import helpers


def get_display(w, h, input_text):
    display = [[0 for _ in xrange(w)] for __ in xrange(h)]

    for line in input_text:
        words = line.split()
        if words[0] == 'rect':
            size = words[1]
            [x, y] = size.split("x")
            for a in xrange(int(y)):
                for b in xrange(int(x)):
                    display[a][b] = 1
            continue
        if words[1] == 'row':
            y = int(words[2][2:])
            amt = int(words[4])
            display[y] = display[y][-amt:] + display[y][:-amt]
            continue

        x = int(words[2][2:])
        amt = int(words[4])
        for _ in xrange(amt):
            holder = display[-1][x]
            for y in xrange(len(display)-1, 0, -1):
                display[y][x] = display[y-1][x]
            display[0][x] = holder
    return display


if __name__ == '__main__':
    final_display = get_display(50, 6, helpers.get_all_lines('day8_input.txt'))
    print sum(map(sum, final_display))
    print ''
    for row in final_display:
        print ''.join(map(lambda x: '##' if x else '  ', row))

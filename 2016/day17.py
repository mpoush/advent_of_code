from hashlib import md5


def get_directions(key, x, y, steps):
    opened = map('bcdef'.__contains__, md5(key).hexdigest()[:4])
    if y > 0 and opened[0]:
        yield (key + 'U', x, y - 1, steps + 1)
    if y < 3 and opened[1]:
        yield (key + 'D', x, y + 1, steps + 1)
    if x > 0 and opened[2]:
        yield (key + 'L', x - 1, y, steps + 1)
    if x < 3 and opened[3]:
        yield (key + 'R', x + 1, y, steps + 1)


def run(key):
    options = [(key, 0, 0, 0)]
    best_path = None
    longest_path = ''
    while options:
        current = options.pop()
        if current[1] == 3 and current[2] == 3:
            path = current[0][len(key):]
            if len(path) > len(longest_path):
                longest_path = path
            if best_path is None or len(path) < len(best_path):
                best_path = path
        else:
            for d in get_directions(*current):
                options.append(d)
    return best_path, len(longest_path)


if __name__ == '__main__':
    print run('ihgpwlah') == ('DDRRRD', 370)
    print run('kglvqrro') == ('DDUDRLRRUDRD', 492)
    print run('ulqzkmiv') == ('DRURDRUDDLLDLUURRDULRLDUUDDDRR', 830)
    print run('pslxynzg')

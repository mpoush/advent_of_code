import helpers


def calculate_distance(instructions, stop_at_first_repeat=False):
    instruction = instructions.split(', ')
    visited = {(0, 0)}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = (0, 0)
    facing = 0
    for i in instruction:
        if i[0] == 'R':
            facing += 1
        else:
            facing += 3
        facing %= 4
        steps = int(i[1:])
        for ix in xrange(steps):
            x, y = helpers.move((x, y), directions[facing])
            p = (x, y)
            if stop_at_first_repeat:
                if p in visited:
                    return abs(x) + abs(y)
                visited.add(p)
    return abs(x) + abs(y)


def first_double(instructions):
    return calculate_distance(instructions, stop_at_first_repeat=True)


if __name__ == '__main__':
    print calculate_distance("R2, L3") == 5
    print calculate_distance("R2, R2, R2") == 2
    print calculate_distance("R5, L5, R5, R3") == 12

    inputString = """
    L1, L3, L5, L3, R1, L4, L5, R1, R3, L5, R1, L3, L2, L3, R2, R2, L3, L3, R1, L2, R1, L3, L2, R4, R2, L5, R4, L5, R4, L2, R3, L2, R4, R1, L5, L4, R1, L2, R3, R1, R2, L4, R1, L2, R3, L2, L3, R5, L192, R4, L5, R4, L1, R4, L4, R2, L5, R45, L2, L5, R4, R5, L3, R5, R77, R2, R5, L5, R1, R4, L4, L4, R2, L4, L1, R191, R1, L1, L2, L2, L4, L3, R1, L3, R1, R5, R3, L1, L4, L2, L3, L1, L1, R5, L4, R1, L3, R1, L2, R1, R4, R5, L4, L2, R4, R5, L1, L2, R3, L4, R2, R2, R3, L2, L3, L5, R3, R1, L4, L3, R4, R2, R2, R2, R1, L4, R4, R1, R2, R1, L2, L2, R4, L1, L2, R3, L3, L5, L4, R4, L3, L1, L5, L3, L5, R5, L5, L4, L2, R1, L2, L4, L2, L4, L1, R4, R4, R5, R1, L4, R2, L4, L2, L4, R2, L4, L1, L2, R1, R4, R3, R2, R2, R5, L1, L2
    """.strip()
    print calculate_distance(inputString) == 299

    print first_double("R8, R4, R4, R8") == 4
    print first_double(inputString)


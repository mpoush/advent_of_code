import helpers


def next_button_square(start, instructions):
    start = int(start)
    for i in instructions:
        if i == 'U' and start > 3:
            start -= 3
        if i == 'D' and start < 7:
            start += 3
        if i == 'L' and start not in {1, 4, 7}:
            start -= 1
        if i == 'R' and start not in {3, 6, 9}:
            start += 1
    return str(start)

from_letter = {}
from_loc = {}


def generate_diamond_buttons():
    diamond = """
  1
 234
56789
 ABC
  D
    """
    for y, row in enumerate(diamond.splitlines()):
        for x, c in enumerate(row):
            if c.strip():
                from_letter[c] = (x, y)
                from_loc[(x, y)] = c


def next_button_diamond(start, instructions):
    if not from_letter:
        generate_diamond_buttons()
    answer = start
    for i in instructions:
        x, y = from_letter[answer]
        if i == 'D':
            y += 1
        elif i == 'U':
            y -= 1
        elif i == 'L':
            x -= 1
        elif i == 'R':
            x += 1
        if (x, y) in from_loc:
            answer = from_loc[(x, y)]
    return answer


def get_code(instruction_set, use_diamond=False):
    method = next_button_diamond if use_diamond else next_button_square
    button = "5"
    result = ""
    for i in instruction_set:
        button = method(button, i)
        result += str(button)
    return result


if __name__ == '__main__':
    sample_instructions = """
ULL
RRDDD
LURDL
UUUUD
    """.strip().splitlines()

    puzzle_input = helpers.get_all_lines('day2_input.txt')

    print get_code(sample_instructions) == "1985"
    print get_code(sample_instructions, use_diamond=True) == "5DB3"
    print get_code(puzzle_input) == "19636"
    print get_code(puzzle_input, use_diamond=True) == "3CC43"

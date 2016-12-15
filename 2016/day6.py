import helpers
from collections import Counter


def get_messages(inputs):
    counters = [Counter() for _ in inputs[0]]

    for row in inputs:
        for ix, c in enumerate(row):
            counters[ix][c] += 1

    return ''.join([c.most_common()[0][0] for c in counters]),\
           ''.join([c.most_common()[-1][0] for c in counters])

if __name__ == '__main__':
    test_inputs = """
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
    """.strip().splitlines()
    print get_messages(test_inputs)
    print get_messages(helpers.get_all_lines('day6_input.txt'))

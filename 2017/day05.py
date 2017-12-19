def count_step(data, second_half=False):
    arrays = data[::]
    ix = 0
    steps = 0
    while 0 <= ix < len(arrays):
        steps += 1
        val = arrays[ix]
        arrays[ix] += -1 if second_half and val > 2 else 1
        ix += val
    return steps

sample = [0,3,0,1,-3]
assert count_step(sample) == 5
assert count_step(sample, True) == 10

with open("day5.txt") as f:
    puzzle = map(int, map(str.strip, f.readlines()))

print count_step(puzzle), 359348
print count_step(puzzle, True), 27688760

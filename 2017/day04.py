def sort_word(word):
    return ''.join(sorted(word))

def part1(phrase):
    return is_valid(phrase, True)

def part2(phrase):
    return is_valid(phrase, False)

def is_valid(phrase, first_half):
    words = phrase.split()
    if not first_half:
        words = map(sort_word, words)
    reduced = set(words)
    return len(reduced) == len(words)

with open("day4.txt") as f:
    pass_list = map(str.strip, f.readlines())

print len(filter(part1, pass_list))
print len(filter(part2, pass_list))

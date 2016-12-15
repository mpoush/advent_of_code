from collections import Counter
import helpers


def verify(code):
    checksum = code[-6:-1]
    code = code[:-7]
    code = str(code)
    sector = code.split("-")[-1]
    code = code[:-len(sector)-1]
    counter = Counter()
    for c in code:
        if c == '-':
            continue
        counter[c] += 1
    chars = ''.join([x for x, _ in sorted(counter.items(), key=lambda (a, b): (-b, a))][:5])
    return code, int(sector), checksum == chars


def translate_single(code, x):
    if x == '-':
        return x
    a = ord(x) - 97
    b = (a + code) % 26
    return chr(b+97)


def translate((room, code, _)):
    returned = map(lambda x: translate_single(code, x), room)
    return ''.join(returned), code


def get_sum(words):
    mapped = map(verify, words)
    real_words = [x for x in mapped if x[2]]
    translated = map(translate, real_words)
    codes = [code for room, code in translated if room == 'northpole-object-storage']
    return sum(code for room, code, real in real_words), codes[-1]


if __name__ == '__main__':
    input_words = helpers.get_all_lines('day4_input.txt')
    sector_sum, sector_id = get_sum(input_words)
    print sector_sum == 245102
    print sector_id == 324

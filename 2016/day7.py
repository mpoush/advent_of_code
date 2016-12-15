import helpers
from itertools import imap, cycle


def yield_parts(string):
    chars = cycle('[[]]')
    while next(chars) in string:
        i = string.find(next(chars))
        yield string[:i]
        string = string[i + 1:]
    yield string


def split_up(string):
    parts = list(yield_parts(string))
    return parts[0::2], parts[1::2]


def get_chunks_of_len(string, size):
    while len(string) >= size:
        if string[0] != string[1]:
            yield string[:size]
        string = string[1:]


def is_abba(string):
    return any(imap(lambda s: s[0] == s[3] and s[1] == s[2], get_chunks_of_len(string, 4)))


def get_babs(ls_array):
    for [a, b, _] in get_abas(ls_array):
        yield ''.join([b, a, b])


def get_abas(ls_array):
    for string in ls_array:
        for c in get_chunks_of_len(string, 3):
            if c[0] == c[2]:
                yield c


def supports_ssl(string):
    outsides, insides = split_up(string)
    bab = set(get_babs(outsides))
    aba = get_abas(insides)
    return any(bab.intersection(aba))


def supports_tls(string):
    outsides, insides = split_up(string)
    return not any(imap(is_abba, insides)) and any(imap(is_abba, outsides))


def solve(ips):
    return len(filter(supports_tls, ips)), len(filter(supports_ssl, ips))

if __name__ == '__main__':
    print solve(helpers.get_all_lines('day7_input.txt')) == (118, 260)

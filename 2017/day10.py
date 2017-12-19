def knot(twists, size=256, times=1):
    ls = list(xrange(size))
    current_pos = 0
    skip = 0
    for _ in xrange(times):
        for twist in twists:
            ls, current_pos, skip = knot_one(ls, current_pos, twist, skip)
    return ls

def knot_one(ls, current_pos, twist, skip):
    if current_pos:
        ls = ls[current_pos:] + ls[:current_pos]
    ls[:twist] = reversed(ls[:twist])
    if current_pos:
        remain = len(ls) - current_pos
        ls = ls[remain:] + ls[:remain]
    current_pos += twist
    current_pos += skip
    skip += 1

    return ls, current_pos % len(ls), skip % len(ls)

def by_sixteen(ls):
    for x in xrange(16):
        yield ls[x*16:x*16+16]

def xor16(ls):
    answer = 0
    for l in ls:
        answer = answer ^ l
    return answer

hexes = [hex(n)[2:].zfill(2) for n in xrange(256)]

def knot_hash_numbers(s):
    twists = map(ord, s) + [17, 31, 73, 47, 23]
    ls = knot(twists, times=64)
    return map(xor16, by_sixteen(ls))

hash_memo = {}
def knot_hash(s):
    if s not in hash_memo:
        sixteens = knot_hash_numbers(s)
        hash_memo[s] = ''.join(map(hexes.__getitem__, sixteens))
    return hash_memo[s]

if __name__ == '__main__':
    ls = knot([197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63])
    print ls[0]*ls[1]

    print knot_hash("197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63")

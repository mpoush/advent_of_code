wall_memo = {}


def count_bits(n):
    answer = 0
    while n:
        answer += 1
        n &= n - 1
    return answer


def is_wall(*args):
    if args in wall_memo:
        return wall_memo[args]
    (x, y), favorite = args
    answer = x * x + 3 * x + 2 * x * y + y + y * y + favorite
    answer = (count_bits(answer) % 2) == 1
    wall_memo[args] = answer
    return answer


def neighbors((x, y)):
    yield (x+1, y)
    yield (x, y+1)
    if x > 0:
        yield (x-1, y)
    if y > 0:
        yield (x, y-1)


def smallest_distance(dest_x, dest_y, favorite):
    dest = (dest_x, dest_y)
    current_level = [(1, 1)]
    seen = set(current_level)
    distance = 0
    under_50 = None
    while True:
        if distance == 50:
            under_50 = len(seen)
        distance += 1
        next_step = []
        while current_level:
            current = current_level.pop()
            for n in neighbors(current):
                if n == dest:
                    return distance, under_50
                if n in seen:
                    continue
                if is_wall(n, favorite):
                    continue
                next_step.append(n)
                seen.add(n)
        current_level = next_step


if __name__ == '__main__':
    print smallest_distance(7, 4, 10) == (11, None)
    print smallest_distance(31, 39, 1362)

from collections import defaultdict

def run(data):
    weights = {}
    children = defaultdict(list)
    parents = {}

    for d in data:
        parts = d.split()
        name = parts[0]
        weight = int(parts[1][1:-1])
        weights[name] = weight
        if len(parts) > 2:
            kids = [x.strip(',') for x in parts[3::1]]
            for k in kids:
                parents[k] = name
            children[name] = kids

    while name in parents:
        name = parents[name]
    root_node = name

    total_weight = {}
    def weight_of(node):
        if node in total_weight:
            return total_weight[node]
        answer = weights[node]
        for child in children[node]:
            answer += weight_of(child)
        total_weight[node] = answer
        return answer

    extra = 0
    while True:
        kids = children[name]
        kids.sort(key=weight_of)
        kids_weights = map(weight_of, kids)

        if(kids_weights[0] == kids_weights[-1]):
            return root_node, weights[name] - extra

        extra = kids_weights[-1] - kids_weights[0]

        if(kids_weights[0] == kids_weights[1]):
            name = kids[-1]
        else:
            name = kids[0]
            extra *= -1

sample = [
    "pbga (66)",
    "xhth (57)",
    "ebii (61)",
    "havc (66)",
    "ktlj (57)",
    "fwft (72) -> ktlj, cntj, xhth",
    "qoyq (66)",
    "padx (45) -> pbga, havc, qoyq",
    "tknk (41) -> ugml, padx, fwft",
    "jptl (61)",
    "ugml (68) -> gyxo, ebii, jptl",
    "gyxo (61)",
    "cntj (57)"
]
assert run(sample) == ('tknk', 60)

with open('day7.txt') as f:
    data = map(str.strip, f.readlines())

print run(data)

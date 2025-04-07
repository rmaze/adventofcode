from collections import defaultdict
import sys


def parse_input():
    lines = sys.stdin.read().strip().split("\n")
    rules = []
    updates = []
    parsing_updates = False

    for line in lines:
        if not line:
            parsing_updates = True
            continue
        if parsing_updates:
            updates.append(list(map(int, line.split(","))))
        else:
            x, y = map(int, line.split("|"))
            rules.append((x, y))

    return rules, updates


def build_dependency_graph(rules):
    graph = defaultdict(set)
    for x, y in rules:
        graph[y].add(x)  # y depends on x
    return graph


def is_valid_order(update, graph):
    position = {num: idx for idx, num in enumerate(update)}
    for y, dependencies in graph.items():
        if y in position:
            for x in dependencies:
                if x in position and position[x] > position[y]:
                    return False
    return True


def find_middle_number(update):
    return update[len(update) // 2]


def main():
    rules, updates = parse_input()
    graph = build_dependency_graph(rules)

    valid_updates = [update for update in updates if is_valid_order(update, graph)]
    middle_sum = sum(find_middle_number(update) for update in valid_updates)

    print(middle_sum)


if __name__ == "__main__":
    main()

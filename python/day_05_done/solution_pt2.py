from collections import defaultdict, deque
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
    reverse_graph = defaultdict(set)

    for x, y in rules:
        graph[x].add(y)
        reverse_graph[y].add(x)

    return graph, reverse_graph


def is_valid_order(update, reverse_graph):
    position = {num: idx for idx, num in enumerate(update)}
    for y, dependencies in reverse_graph.items():
        if y in position:
            for x in dependencies:
                if x in position and position[x] > position[y]:
                    return False
    return True


def find_middle_number(update):
    return update[len(update) // 2] if update else 0


def topological_sort(update, graph, reverse_graph):
    subset = set(update)
    temp_graph = defaultdict(set)
    in_degree = defaultdict(int)

    for x in subset:
        for y in graph[x]:
            if y in subset:
                temp_graph[x].add(y)
                in_degree[y] += 1
        if x not in in_degree:
            in_degree[x] = 0

    queue = deque(sorted([node for node in subset if in_degree[node] == 0]))
    sorted_list = []

    while queue:
        node = queue.popleft()
        sorted_list.append(node)
        for neighbor in temp_graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_list if len(sorted_list) == len(subset) else sorted(update)


def main():
    rules, updates = parse_input()
    graph, reverse_graph = build_dependency_graph(rules)

    valid_updates = []
    invalid_updates = []

    for update in updates:
        if is_valid_order(update, reverse_graph):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    middle_sum_valid = sum(find_middle_number(update) for update in valid_updates)

    corrected_updates = [
        topological_sort(update, graph, reverse_graph) for update in invalid_updates
    ]
    middle_sum_corrected = sum(
        find_middle_number(update) for update in corrected_updates
    )

    print("Part 1:", middle_sum_valid)
    print("Part 2:", middle_sum_corrected)


if __name__ == "__main__":
    main()

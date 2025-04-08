from collections import defaultdict, deque


def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        lines = file.read().strip().split("\n")
    rules = []
    updates = []
    parsing_updates = False
    for line in lines:
        if not line:
            parsing_updates = True
            continue
        if parsing_updates:
            updates.append([int(n) for n in line.split(",")])
        else:
            x, y = map(int, line.split("|"))
            rules.append((x, y))
    graph = defaultdict(set)
    reverse_graph = defaultdict(set)
    for x, y in rules:
        graph[x].add(y)
        reverse_graph[y].add(x)
    # Filter out updates that are not in valid dependency order
    invalid_updates = []
    for update in updates:
        valid = True
        pos = {num: idx for idx, num in enumerate(update)}
        for y, deps in reverse_graph.items():
            if y in pos:
                for x in deps:
                    if x in pos and pos[x] > pos[y]:
                        valid = False
                        break
            if not valid:
                break
        if not valid:
            invalid_updates.append(update)

    # Inner function to perform topological sort on an update.
    def topo_sort(update):
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
        q = deque(sorted(n for n in subset if in_degree[n] == 0))
        sorted_list = []
        while q:
            node = q.popleft()
            sorted_list.append(node)
            for neigh in temp_graph[node]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    q.append(neigh)
        return sorted_list if len(sorted_list) == len(subset) else sorted(update)

    # Correct invalid updates
    corrected_updates = [topo_sort(update) for update in invalid_updates]
    # For each corrected update, select the middle element.
    middle_sum_corrected = sum(update[len(update) // 2] for update in corrected_updates)
    print(middle_sum_corrected)


if __name__ == "__main__":
    main()

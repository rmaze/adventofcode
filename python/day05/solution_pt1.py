from collections import defaultdict


def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
    rules, updates = [], []
    parsing_updates = False
    for line in lines:
        if not line.strip():
            parsing_updates = True
            continue
        if parsing_updates:
            updates.append([int(num) for num in line.split(",")])
        else:
            x, y = map(int, line.split("|"))
            rules.append((x, y))
    graph = defaultdict(set)
    for x, y in rules:
        graph[y].add(x)
    valid_updates = []
    for update in updates:
        pos = {num: idx for idx, num in enumerate(update)}
        valid = True
        for y, deps in graph.items():
            if y in pos:
                for x in deps:
                    if x in pos and pos[x] > pos[y]:
                        valid = False
                        break
            if not valid:
                break
        if valid:
            valid_updates.append(update)
    middle_sum = sum(update[len(update) // 2] for update in valid_updates)
    print(middle_sum)


if __name__ == "__main__":
    main()

def is_strictly_safe(levels):
    if len(levels) < 2:
        return True
    diffs = []
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        if diff == 0 or abs(diff) > 3:
            return False
        diffs.append(diff)
    all_pos = all(d > 0 for d in diffs)
    all_neg = all(d < 0 for d in diffs)
    return all_pos or all_neg


def is_safe_with_dampener(levels):
    if is_strictly_safe(levels):
        return True
    for i in range(len(levels)):
        modified = levels[:i] + levels[i + 1 :]
        if is_strictly_safe(modified):
            return True
    return False


def main():
    with open("input.txt", "r") as file:
        lines = file.read().strip().splitlines()
    safe_count = 0
    for line in lines:
        levels = list(map(int, line.split()))
        if is_safe_with_dampener(levels):
            safe_count += 1
    print(safe_count)


if __name__ == "__main__":
    main()

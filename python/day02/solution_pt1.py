def is_safe_report(levels):
    diffs = []
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        diffs.append(diff)
    for d in diffs:
        if d == 0 or abs(d) < 1 or abs(d) > 3:
            return False
    all_positive = all(d > 0 for d in diffs)
    all_negative = all(d < 0 for d in diffs)
    return all_positive or all_negative


def main():
    with open("input.txt", "r") as file:
        lines = file.read().strip().splitlines()
    safe_count = 0
    for line in lines:
        levels = list(map(int, line.split()))
        if is_safe_report(levels):
            safe_count += 1
    print(safe_count)


if __name__ == "__main__":
    main()

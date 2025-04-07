import sys


def is_strictly_safe(levels):
    """
    Checks if the levels are strictly increasing or strictly decreasing
    with each absolute consecutive difference between 1 and 3 (inclusive).
    """
    if len(levels) < 2:
        # A single-level or empty report is trivially safe,
        # but the puzzle's context suggests we have at least 2 levels per report.
        return True

    diffs = []
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        # Must be strictly positive or strictly negative (non-zero)
        # and magnitude in [1..3]
        if diff == 0 or abs(diff) > 3:
            return False
        diffs.append(diff)

    # Check if all diffs are positive or all diffs are negative
    all_pos = all(d > 0 for d in diffs)
    all_neg = all(d < 0 for d in diffs)
    return all_pos or all_neg


def is_safe_with_dampener(levels):
    """
    Determines if a report is safe either as-is
    or by removing one level (Problem Dampener).
    """
    # 1) Check if already strictly safe
    if is_strictly_safe(levels):
        return True

    # 2) Try removing each level once
    for i in range(len(levels)):
        # Create a new list with the i-th element removed
        modified = levels[:i] + levels[i + 1 :]
        if is_strictly_safe(modified):
            return True

    return False


def solve():
    lines = sys.stdin.read().strip().splitlines()
    safe_count = 0

    for line in lines:
        levels = list(map(int, line.split()))
        if is_safe_with_dampener(levels):
            safe_count += 1

    print(safe_count)


if __name__ == "__main__":
    solve()

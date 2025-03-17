import sys

def is_safe_report(levels):
    # Determine if the report is strictly increasing or strictly decreasing
    diffs = []
    
    for i in range(len(levels) - 1):
        diff = levels[i+1] - levels[i]
        diffs.append(diff)
    
    # Check that all differences are nonzero (strictly increasing or decreasing)
    # and that the absolute difference is between 1 and 3 inclusive
    for d in diffs:
        if d == 0 or abs(d) < 1 or abs(d) > 3:
            return False
    
    # Now check if either all positive or all negative
    all_positive = all(d > 0 for d in diffs)
    all_negative = all(d < 0 for d in diffs)
    
    return all_positive or all_negative

def solve():
    lines = sys.stdin.read().strip().splitlines()
    safe_count = 0
    for line in lines:
        # Parse each line into integers
        levels = list(map(int, line.split()))
        if is_safe_report(levels):
            safe_count += 1
    
    print(safe_count)

if __name__ == "__main__":
    solve()
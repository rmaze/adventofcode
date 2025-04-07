import sys


def solve():
    # Read all lines (the puzzle grid)
    grid = [line.strip() for line in sys.stdin if line.strip()]
    if not grid:
        print(0)
        return

    rows = len(grid)
    cols = len(grid[0])

    count_xmas = 0

    # We need at least 3 rows and 3 columns to form a 3x3 X
    if rows < 3 or cols < 3:
        print(0)
        return

    # For convenience, define valid corner pairs
    valid_corners = {("M", "S"), ("S", "M")}

    # Check each cell to see if it can be the center of an X
    for r in range(1, rows - 1):  # center row can't be topmost or bottommost
        for c in range(1, cols - 1):  # center col can't be leftmost or rightmost
            if grid[r][c] != "A":
                continue  # skip if center is not 'A'

            # Collect the 4 corners around (r, c)
            top_left = grid[r - 1][c - 1]
            bottom_right = grid[r + 1][c + 1]
            top_right = grid[r - 1][c + 1]
            bottom_left = grid[r + 1][c - 1]

            # Diagonal #1 corners -> (top_left, bottom_right)
            if (top_left, bottom_right) not in valid_corners:
                continue

            # Diagonal #2 corners -> (top_right, bottom_left)
            if (top_right, bottom_left) not in valid_corners:
                continue

            # If both diagonals match the pattern, count one X-MAS
            count_xmas += 1

    print(count_xmas)


if __name__ == "__main__":
    solve()

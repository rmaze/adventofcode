from collections import defaultdict


def read_map(filename: str) -> list[list[int]]:
    """
    Reads a topographic map from a text file.
    Each line is a string of digits '0'..'9'.
    Returns a 2D list (grid) of integers.
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    grid = [[int(ch) for ch in line] for line in lines]
    return grid


def neighbors(r: int, c: int, rows: int, cols: int):
    """Return the four orthogonal neighbors (up, down, left, right) in-bounds."""
    if r > 0:
        yield (r - 1, c)
    if r < rows - 1:
        yield (r + 1, c)
    if c > 0:
        yield (r, c - 1)
    if c < cols - 1:
        yield (r, c + 1)


def compute_dp_paths_to_9(grid: list[list[int]]) -> list[list[int]]:
    """
    Returns a 2D list dp[r][c], where dp[r][c] is the number of distinct
    ways to reach a cell of height 9 from (r,c) by stepping +1 in height
    at each move (only up/down/left/right).
    """
    rows = len(grid)
    cols = len(grid[0])
    dp = [[0] * cols for _ in range(rows)]

    # Group cells by their height for easy iteration from 9 down to 0
    height_map = defaultdict(list)
    for r in range(rows):
        for c in range(cols):
            h = grid[r][c]
            height_map[h].append((r, c))

    # 1) Initialize dp = 1 for all cells of height 9
    for r, c in height_map[9]:
        dp[r][c] = 1

    # 2) For heights h from 8 down to 0, fill dp using the formula:
    #    dp[r][c] = sum of dp[nr][nc] for neighbors (nr,nc) where grid[nr][nc] == h+1.
    for h in range(8, -1, -1):  # 8 down to 0
        for r, c in height_map[h]:
            ways = 0
            for nr, nc in neighbors(r, c, rows, cols):
                if grid[nr][nc] == h + 1:
                    ways += dp[nr][nc]
            dp[r][c] = ways

    return dp


def solve_day10_rating(filename: str) -> int:
    """
    Read the map from 'filename', compute how many distinct paths lead from each cell
    to some cell of height 9 (by ascending +1 each step).
    Then the rating for a trailhead (height=0) is dp[r][c].
    Return the sum of ratings for all trailheads.
    """
    grid = read_map(filename)
    dp = compute_dp_paths_to_9(grid)

    rows = len(grid)
    cols = len(grid[0])

    total_rating = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                # This cell is a trailhead; dp[r][c] is its rating
                total_rating += dp[r][c]

    return total_rating


def main():
    filename = "input.txt"
    answer = solve_day10_rating(filename)
    print("Sum of the ratings of all trailheads:", answer)


if __name__ == "__main__":
    main()

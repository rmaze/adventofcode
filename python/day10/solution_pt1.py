from collections import deque


def read_map(filename: str) -> list[list[int]]:
    """
    Reads a topographic map from a text file.
    Each line is a string of digits '0'..'9'.
    Returns a 2D list (grid) of integers.
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    # Convert each line's characters to integers
    return [[int(ch) for ch in line] for line in lines]


def neighbors(r: int, c: int, rows: int, cols: int) -> list[tuple[int, int]]:
    """
    Returns valid 4-directional neighbors (up/down/left/right) of (r, c)
    within the grid bounds.
    """
    result = []
    if r > 0:
        result.append((r - 1, c))
    if r < rows - 1:
        result.append((r + 1, c))
    if c > 0:
        result.append((r, c - 1))
    if c < cols - 1:
        result.append((r, c + 1))
    return result


def bfs_trail_score(grid: list[list[int]], start_r: int, start_c: int) -> int:
    """
    From the given trailhead (which has height 0), do a BFS (or DFS) over
    all cells reachable by ascending exactly +1 in height each step.
    Return the number of unique positions of height 9 reached.
    """
    rows = len(grid)
    cols = len(grid[0])
    start_height = grid[start_r][start_c]
    assert start_height == 0, "Starting cell must have height 0."

    visited = [[False] * cols for _ in range(rows)]
    visited[start_r][start_c] = True
    queue = deque()
    queue.append((start_r, start_c))

    reached_nines = 0
    # We'll keep track whether we've visited a 9-cell once. A boolean check is enough
    # if we’re only counting unique positions of height 9.
    nine_visited = set()

    while queue:
        r, c = queue.popleft()
        current_height = grid[r][c]

        # If this position is height 9, record it
        if current_height == 9 and (r, c) not in nine_visited:
            nine_visited.add((r, c))
            reached_nines += 1

        # Explore neighbors that are exactly +1 in height
        next_height = current_height + 1
        for nr, nc in neighbors(r, c, rows, cols):
            if not visited[nr][nc] and grid[nr][nc] == next_height:
                visited[nr][nc] = True
                queue.append((nr, nc))

    return reached_nines


def solve_day10(filename: str) -> int:
    """
    Main solver that reads a topographic map from 'filename',
    identifies all trailheads (height=0), computes each trailhead's score,
    and returns the sum of the scores.
    """
    grid = read_map(filename)
    rows = len(grid)
    cols = len(grid[0])

    total_score = 0

    # Identify trailheads (cells of height 0)
    trailheads = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                trailheads.append((r, c))

    # Compute score for each trailhead and accumulate
    for r, c in trailheads:
        score = bfs_trail_score(grid, r, c)
        total_score += score

    return total_score


def main():
    # Example usage: reading "input.txt" as the topographic map
    filename = "input.txt"
    answer = solve_day10(filename)
    print("Sum of the scores of all trailheads:", answer)


if __name__ == "__main__":
    main()

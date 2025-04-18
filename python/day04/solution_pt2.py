def solve():
    with open("input.txt", "r") as file:
        grid = [line.strip() for line in file if line.strip()]
    if not grid:
        print(0)
        return
    rows = len(grid)
    cols = len(grid[0])
    count_xmas = 0
    if rows < 3 or cols < 3:
        print(0)
        return
    valid_corners = {("M", "S"), ("S", "M")}
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] != "A":
                continue
            top_left = grid[r - 1][c - 1]
            bottom_right = grid[r + 1][c + 1]
            top_right = grid[r - 1][c + 1]
            bottom_left = grid[r + 1][c - 1]
            if (top_left, bottom_right) not in valid_corners:
                continue
            if (top_right, bottom_left) not in valid_corners:
                continue
            count_xmas += 1
    print(count_xmas)


if __name__ == "__main__":
    solve()

import sys


def solve():
    grid = [line.strip() for line in sys.stdin if line.strip()]
    if not grid:
        print(0)
        return

    rows = len(grid)
    cols = len(grid[0])
    target = "XMAS"
    t_len = len(target)

    # (Δrow, Δcol) for the 8 directions
    directions = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, -1),  # diagonal up-left
        (-1, 1),  # diagonal up-right
        (1, -1),  # diagonal down-left
        (1, 1),  # diagonal down-right
    ]

    # Collect coordinates of all 'X' cells
    x_positions = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "X":
                x_positions.append((r, c))

    count = 0

    # For each 'X' cell, try to match the rest of "MAS" in all directions
    for r, c in x_positions:
        for dr, dc in directions:
            # End cell = start + (t_len - 1) steps in (dr, dc)
            end_r = r + dr * (t_len - 1)
            end_c = c + dc * (t_len - 1)
            # Check boundaries
            if 0 <= end_r < rows and 0 <= end_c < cols:
                # Collect letters along this direction
                found = True
                rr, cc = r, c
                for i in range(t_len):
                    if grid[rr][cc] != target[i]:
                        found = False
                        break
                    rr += dr
                    cc += dc
                if found:
                    count += 1

    print(count)


if __name__ == "__main__":
    solve()

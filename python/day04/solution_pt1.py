def main() -> int:
    """
    Reads a grid from 'input.txt' and counts the number of occurrences
    of the target word "XMAS" in all 8 directions starting from a cell containing 'X'.

    Returns:
        int: The total count of occurrences of "XMAS" found in the grid.
    """
    with open("input.txt", "r", encoding="utf-8") as file:
        grid: list[str] = [line.strip() for line in file if line.strip()]
    if not grid:
        return 0

    num_rows: int = len(grid)
    num_cols: int = len(grid[0])
    target: str = "XMAS"
    target_len: int = len(target)
    directions: list[tuple[int, int]] = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]

    x_positions: list[tuple[int, int]] = [
        (r, c) for r in range(num_rows) for c in range(num_cols) if grid[r][c] == "X"
    ]

    count: int = 0
    for start_row, start_col in x_positions:
        for dr, dc in directions:
            end_row = start_row + dr * (target_len - 1)
            end_col = start_col + dc * (target_len - 1)
            if not (0 <= end_row < num_rows and 0 <= end_col < num_cols):
                continue
            found: bool = True
            row, col = start_row, start_col
            for char in target:
                if grid[row][col] != char:
                    found = False
                    break
                row += dr
                col += dc
            if found:
                count += 1

    return count


if __name__ == "__main__":
    result: int = main()
    print(result)

def parse_map(grid):
    guard_position = None
    guard_direction = None

    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in directions:
                guard_position = (r, c)
                guard_direction = directions[cell]
                grid[r] = grid[r][:c] + "." + grid[r][c + 1 :]  # Remove guard symbol
                break
        if guard_position:
            break

    return grid, guard_position, guard_direction


def simulate_patrol(grid, start_pos, start_dir):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    pos = start_pos
    direction = start_dir

    turn_right = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}

    while 0 <= pos[0] < rows and 0 <= pos[1] < cols:
        visited.add(pos)
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])

        if (
            0 <= new_pos[0] < rows
            and 0 <= new_pos[1] < cols
            and grid[new_pos[0]][new_pos[1]] != "#"
        ):
            pos = new_pos  # Move forward
        else:
            direction = turn_right[direction]  # Turn right

    return len(visited)


def main():
    from sys import stdin

    grid = [line.strip() for line in stdin.readlines()]
    grid, start_pos, start_dir = parse_map(grid)
    result = simulate_patrol(grid, start_pos, start_dir)
    print(result)


if __name__ == "__main__":
    main()

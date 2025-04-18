def solve():
    import sys

    # Read all lines (the entire map)
    lines = [line.rstrip("\n") for line in sys.stdin.readlines()]

    # Dimensions
    R = len(lines)
    C = len(lines[0]) if R > 0 else 0

    # Directions for convenience
    # We'll map the guard symbol to (dr, dc)
    dir_map = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

    # Function to turn right (dr, dc) -> new (dr, dc)
    def turn_right(direction):
        (dr, dc) = direction
        # Up -> Right
        if (dr, dc) == (-1, 0):
            return (0, 1)
        # Right -> Down
        if (dr, dc) == (0, 1):
            return (1, 0)
        # Down -> Left
        if (dr, dc) == (1, 0):
            return (0, -1)
        # Left -> Up
        if (dr, dc) == (0, -1):
            return (-1, 0)

    # Find guard's starting position and direction
    start_r = start_c = None
    direction = None

    for r in range(R):
        for c in range(C):
            ch = lines[r][c]
            if ch in dir_map:
                start_r, start_c = r, c
                direction = dir_map[ch]
                break
        if start_r is not None:
            break

    # Set of visited cells
    visited = set()
    visited.add((start_r, start_c))

    # Current position
    r, c = start_r, start_c
    dr, dc = direction

    # Simulate until we leave the map
    while 0 <= r < R and 0 <= c < C:
        # Check cell in front
        front_r = r + dr
        front_c = c + dc

        # If the next front cell is inside the map and is '#', turn right
        if 0 <= front_r < R and 0 <= front_c < C and lines[front_r][front_c] == "#":
            dr, dc = turn_right((dr, dc))
        else:
            # Step forward
            r, c = front_r, front_c
            # If still inside the map, record this new cell
            if 0 <= r < R and 0 <= c < C:
                visited.add((r, c))

    # Print the number of distinct positions visited
    print(len(visited))


if __name__ == "__main__":
    solve()

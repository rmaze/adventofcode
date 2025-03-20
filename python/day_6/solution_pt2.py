import sys
import multiprocessing

# Global variables for multiprocessing
GRID = []
OBSTACLES = set()
R = C = 0
START_R = START_C = 0
START_DIR = (0, 0)

# Direction rotations
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIR_MAP = {'^': 0, '>': 1, 'v': 2, '<': 3}

def init_globals(grid, obstacles, rows, cols, start_r, start_c, start_dir):
    global GRID, OBSTACLES, R, C, START_R, START_C, START_DIR
    GRID = grid
    OBSTACLES = obstacles
    R, C = rows, cols
    START_R, START_C, START_DIR = start_r, start_c, start_dir

def simulate_guard_with_obstacle(candidate):
    obst = candidate
    r, c = START_R, START_C
    dir_idx = START_DIR

    visited_states = set()
    while True:
        state = (r, c, dir_idx)
        if state in visited_states:
            return True
        visited_states.add(state)

        dr, dc = DIRS[dir_idx]
        fr, fc = r + dr, c + dc

        if not (0 <= fr < R and 0 <= fc < C):
            return False

        if (fr, fc) == obst or (fr, fc) in OBSTACLES:
            dir_idx = (dir_idx + 1) % 4  # rotate right quickly
        else:
            r, c = fr, fc

def solve_part_two_parallel():
    lines = [line.rstrip("\n") for line in sys.stdin]
    rows, cols = len(lines), len(lines[0]) if lines else 0

    grid = [list(line) for line in lines]
    obstacles = {(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == '#'}

    # Locate guard
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in DIR_MAP:
                start_r, start_c, start_dir = r, c, DIR_MAP[grid[r][c]]
                break

    # Candidates are non-obstacle, non-guard cells
    candidates = [(r, c) for r in range(rows) for c in range(cols)
                  if grid[r][c] == '.' and (r, c) != (start_r, start_c)]

    # Initialize globals for fast access by workers
    with multiprocessing.Pool(initializer=init_globals,
                              initargs=(grid, obstacles, rows, cols, start_r, start_c, start_dir)) as pool:
        results = pool.map(simulate_guard_with_obstacle, candidates)

    print(sum(results))

if __name__ == "__main__":
    solve_part_two_parallel()
from collections import defaultdict
import sys


def parse_input() -> tuple[list[str], dict[str, list[tuple[int, int]]]]:
    grid = [line.strip() for line in sys.stdin if line.strip()]
    antennas: dict[str, list[tuple[int, int]]] = defaultdict(list)

    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char != ".":
                antennas[char].append((r, c))

    return grid, antennas


def find_antinodes(grid: list[str], antennas: dict[str, list[tuple[int, int]]]) -> int:
    R, C = len(grid), len(grid[0])
    antinodes: set[tuple[int, int]] = set()

    for points in antennas.values():
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue

                r1, c1 = points[i]
                r2, c2 = points[j]

                dr, dc = r2 - r1, c2 - c1

                ar1, ac1 = r1 - dr, c1 - dc
                ar2, ac2 = r2 + dr, c2 + dc

                if 0 <= ar1 < R and 0 <= ac1 < C:
                    antinodes.add((ar1, ac1))
                if 0 <= ar2 < R and 0 <= ac2 < C:
                    antinodes.add((ar2, ac2))

    return len(antinodes)


def main() -> None:
    grid, antennas = parse_input()
    total_antinodes = find_antinodes(grid, antennas)
    print(total_antinodes)


if __name__ == "__main__":
    main()

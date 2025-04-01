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


def is_collinear(p1: tuple[int, int], p2: tuple[int, int], p3: tuple[int, int]) -> bool:
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) == (p3[0] - p1[0]) * (p2[1] - p1[1])


def find_antinodes(grid: list[str], antennas: dict[str, list[tuple[int, int]]]) -> int:
    R, C = len(grid), len(grid[0])
    antinodes: set[tuple[int, int]] = set()

    for points in antennas.values():
        if len(points) < 2:
            continue

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                for k in range(R):
                    for m in range(C):
                        if is_collinear(p1, p2, (k, m)):
                            antinodes.add((k, m))

    return len(antinodes)


def main() -> None:
    grid, antennas = parse_input()
    total_antinodes = find_antinodes(grid, antennas)
    print(total_antinodes)


if __name__ == "__main__":
    main()

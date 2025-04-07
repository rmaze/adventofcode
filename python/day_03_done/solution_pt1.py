import sys
import re

PATTERN = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")


def solve():
    data = sys.stdin.read()
    matches = PATTERN.findall(data)

    total_sum = 0
    for x_str, y_str in matches:
        x = int(x_str)
        y = int(y_str)
        total_sum += x * y

    print(total_sum)


if __name__ == "__main__":
    solve()

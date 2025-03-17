import sys
import re

# One pattern to match exactly "do()" or "don't()" or "mul(X,Y)" with 1-3 digit integers.
PATTERN = re.compile(r"(?:do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))")

def solve():
    # Read the entire input
    data = sys.stdin.read()

    # Find all tokens in the order they appear
    tokens = PATTERN.findall(data)

    # At the beginning, mul instructions are enabled
    mul_enabled = True
    total_sum = 0

    for token in tokens:
        if token == "do()":
            # Enable mul instructions
            mul_enabled = True
        elif token == "don't()":
            # Disable mul instructions
            mul_enabled = False
        else:
            # Must be a mul(...) instruction
            # e.g. "mul(44,46)" – parse out the numbers
            if mul_enabled:
                # Extract "44,46" from "mul(44,46)"
                inside = str(token[4:-1])      # remove "mul(" and the trailing ")"
                x_str, y_str = inside.split(",")
                x, y = int(x_str), int(y_str)
                total_sum += x * y

    print(total_sum)

if __name__ == "__main__":
    solve()
def transform_stone(stone_str):
    """
    Given a stone's engraving as a string, apply exactly one rule:
      1) If the stone is '0', it becomes a single stone with '1'.
      2) If the number of digits is even, split into two stones.
      3) Otherwise, multiply the stone by 2024 and return it as a single stone.
    """
    # Rule 1: If the stone is '0'
    if stone_str == "0":
        return ["1"]

    # Rule 2: If the number of digits is even, split into two stones
    length = len(stone_str)
    if length % 2 == 0:
        half = length // 2
        left_digits, right_digits = stone_str[:half], stone_str[half:]
        # Convert to int to remove leading zeros, then back to string
        left_part = str(int(left_digits))
        right_part = str(int(right_digits))
        return [left_part, right_part]

    # Rule 3: Otherwise, multiply by 2024
    num = int(stone_str)
    multiplied = num * 2024
    return [str(multiplied)]


def blink(stones):
    """
    Applies one 'blink' to a list of stones.
    Each stone is transformed according to transform_stone,
    and the results are flattened into a new list of stones.
    """
    new_stones = []
    for stone in stones:
        new_stones.extend(transform_stone(stone))
    return new_stones


def main():
    # Read the initial arrangement from 'input.txt'
    with open("input.txt", "r") as f:
        line = f.readline().strip()

    # Split the line into stone engravings
    stones = line.split()  # list of strings, e.g. ["125", "17"]

    # Blink 25 times
    for _ in range(25):
        stones = blink(stones)

    # Print how many stones remain
    print(len(stones))


if __name__ == "__main__":
    main()

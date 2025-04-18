def extract_tokens(data: str) -> list[str]:
    """
    Extract tokens from the input string.

    Recognized tokens are:
      - "don't()"
      - "do()"
      - "mul(X,Y)" where X and Y are 1–3 digit integers.

    Args:
      data (str): The input data.

    Returns:
      list[str]: A list of tokens in the order they appear in the input.
    """
    tokens = []
    pos = 0
    data_length = len(data)
    while pos < data_length:
        # Check "don't()" first since it starts with "do()"
        if data.startswith("don't()", pos):
            tokens.append("don't()")
            pos += 7
        elif data.startswith("do()", pos):
            tokens.append("do()")
            pos += 4
        elif data.startswith("mul(", pos):
            end_idx = data.find(")", pos)
            if end_idx != -1:
                candidate = data[pos : end_idx + 1]
                inside = candidate[4:-1]
                parts = inside.split(",")
                if (
                    len(parts) == 2
                    and parts[0].isdigit()
                    and parts[1].isdigit()
                    and 1 <= len(parts[0]) <= 3
                    and 1 <= len(parts[1]) <= 3
                ):
                    tokens.append(candidate)
                    pos = end_idx + 1
                else:
                    pos += 1
            else:
                pos += 1
        else:
            pos += 1
    return tokens


def main(data: str) -> int:
    """
    Process the input data and compute the total sum.

    The data contains instruction tokens:
      - "do()": Enables multiplication instructions.
      - "don't()": Disables multiplication instructions.
      - "mul(X,Y)": If multiplication instructions are enabled, the product of X and Y is added to the total sum.

    Args:
      data (str): The input data.

    Returns:
      int: The total sum computed from the valid "mul(X,Y)" tokens.
    """
    tokens = extract_tokens(data)
    mul_enabled = True
    total_sum = 0
    for token in tokens:
        if token == "do()":
            mul_enabled = True
        elif token == "don't()":
            mul_enabled = False
        elif token.startswith("mul(") and token.endswith(")"):
            inside = token[4:-1]
            parts = inside.split(",")
            try:
                x = int(parts[0])
                y = int(parts[1])
            except (ValueError, IndexError):
                continue
            if mul_enabled:
                total_sum += x * y
    return total_sum


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()
    print(main(data))

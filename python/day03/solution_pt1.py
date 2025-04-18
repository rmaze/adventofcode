def main():
    with open("input.txt", "r") as file:
        data = file.read()
    total_sum = 0
    for part in data.split("mul(")[1:]:
        close_paren_index = part.find(")")
        if close_paren_index != -1:
            numbers = part[:close_paren_index].split(",")
            if len(numbers) == 2:
                try:
                    total_sum += int(numbers[0]) * int(numbers[1])
                except ValueError:
                    continue
    print(total_sum)


if __name__ == "__main__":
    main()

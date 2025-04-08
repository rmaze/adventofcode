def main():
    with open("input.txt", "r") as file:
        lines = file.read().strip().splitlines()

    left_list = []
    right_list = []

    for line in lines:
        left_val_str, right_val_str = line.split()
        left_val = int(left_val_str)
        right_val = int(right_val_str)
        left_list.append(left_val)
        right_list.append(right_val)

    left_list.sort()
    right_list.sort()

    total_distance = 0
    for l_val, r_val in zip(left_list, right_list):
        total_distance += abs(l_val - r_val)

    print(total_distance)


if __name__ == "__main__":
    main()

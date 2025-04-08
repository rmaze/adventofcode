from collections import Counter


def main():
    with open("input.txt", "r") as file:
        lines = file.read().strip().splitlines()

    left_list = []
    right_list = []
    for line in lines:
        l_str, r_str = line.split()
        left_list.append(int(l_str))
        right_list.append(int(r_str))

    freq_right = Counter(right_list)
    similarity_score = 0
    for l_val in left_list:
        similarity_score += l_val * freq_right.get(l_val, 0)

    print(similarity_score)


if __name__ == "__main__":
    main()

import sys
import logging


def solve():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s"
    )

    logging.info("Reading input lines from stdin...")
    lines = sys.stdin.read().strip().splitlines()
    logging.info(f"Number of lines read: {len(lines)}")

    left_list = []
    right_list = []

    logging.info("Parsing lines into two lists...")
    for idx, line in enumerate(lines):
        left_val_str, right_val_str = line.split()
        left_val = int(left_val_str)
        right_val = int(right_val_str)
        left_list.append(left_val)
        right_list.append(right_val)
        logging.debug(f"Line {idx + 1}: left={left_val}, right={right_val}")

    logging.info("Sorting the lists...")
    left_list.sort()
    right_list.sort()

    logging.info("Calculating total distance...")
    total_distance = 0
    for l_val, r_val in zip(left_list, right_list):
        distance = abs(l_val - r_val)
        total_distance += distance
        logging.debug(f"Pair: (left={l_val}, right={r_val}), distance={distance}")

    logging.info(f"Total distance: {total_distance}")
    print(total_distance)


if __name__ == "__main__":
    solve()

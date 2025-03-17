import sys
import logging
from collections import Counter

def solve():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

    logging.info("Reading input lines from stdin...")
    lines = sys.stdin.read().strip().splitlines()
    logging.info(f"Number of lines read: {len(lines)}")

    left_list = []
    right_list = []

    logging.info("Parsing lines into two lists...")
    for idx, line in enumerate(lines):
        l_str, r_str = line.split()
        left_list.append(int(l_str))
        right_list.append(int(r_str))
        logging.debug(f"Line {idx+1}: left={l_str}, right={r_str}")

    freq_right = Counter(right_list)
    logging.info("Built frequency map for right list.")

    # Compute similarity score
    logging.info("Calculating similarity score...")
    similarity_score = 0
    for l_val in left_list:
        similarity_score += l_val * freq_right.get(l_val, 0)
        logging.debug(f"Value={l_val}, RightCount={freq_right.get(l_val, 0)}, "
                      f"CurrentSum={l_val * freq_right.get(l_val, 0)}")

    logging.info(f"Final similarity score: {similarity_score}")
    print(similarity_score)

if __name__ == "__main__":
    solve()
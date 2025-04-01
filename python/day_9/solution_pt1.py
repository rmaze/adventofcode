def parse_disk_map(disk_map_str: str) -> list:
    """
    Given a dense-format disk map string, parse and return a list where:
      - Integer values represent file IDs
      - '.' (dot) represents free space.
    """
    blocks = []
    file_id = 0
    is_file_length = True
    
    for ch in disk_map_str:
        length = int(ch)
        if is_file_length:
            # 'length' is a file length for the current file_id
            blocks.extend([file_id] * length)
            file_id += 1
        else:
            # 'length' is free space
            blocks.extend(['.'] * length)
        is_file_length = not is_file_length

    return blocks


def compact_disk(blocks: list) -> None:
    """
    Modifies the list of blocks in place by moving file blocks from the rightmost
    position to the leftmost free-space '.' until there are no more gaps among
    file blocks.
    """
    while True:
        # Find the index of the rightmost file block (any position not '.')
        try:
            rightmost_file_idx = max(i for i, b in enumerate(blocks) if b != '.')
        except ValueError:
            # No file blocks at all; nothing to compact
            break
        
        # Find the leftmost '.' (free space) that is to the left of this rightmost file block
        leftmost_dot_idx = None
        for i in range(rightmost_file_idx):
            if blocks[i] == '.':
                leftmost_dot_idx = i
                break
        
        if leftmost_dot_idx is None:
            # No free space lies to the left of a file block => fully compacted
            break
        
        # Move one file block from the rightmost position to the leftmost gap
        blocks[leftmost_dot_idx] = blocks[rightmost_file_idx]
        blocks[rightmost_file_idx] = '.'


def compute_checksum(blocks: list) -> int:
    """
    Given a list of blocks (where integers represent file IDs and '.' is free space),
    return the sum of (position * file_id) for all file blocks.
    """
    checksum = 0
    for pos, val in enumerate(blocks):
        if val != '.':
            checksum += pos * val
    return checksum


def main():
    # Read the disk map from input.txt
    with open("input.txt", "r", encoding="utf-8") as f:
        disk_map_str = f.read().strip()

    # 1. Parse the dense disk map
    blocks = parse_disk_map(disk_map_str)

    # 2. Compact the disk
    compact_disk(blocks)

    # 3. Compute checksum
    result = compute_checksum(blocks)

    print("Final Checksum:", result)


if __name__ == "__main__":
    main()
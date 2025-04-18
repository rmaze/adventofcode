def parse_disk_map(disk_map_str: str) -> list:
    """
    Expand the dense disk map string into a list of blocks:
      - Integer values (file IDs) for file blocks
      - '.' (dot) for free space
    """
    blocks = []
    file_id = 0
    is_file_length = True

    for ch in disk_map_str:
        length = int(ch)
        if is_file_length:
            # 'length' represents file blocks for this file_id
            blocks.extend([file_id] * length)
            file_id += 1
        else:
            # 'length' represents free space
            blocks.extend(["."] * length)
        is_file_length = not is_file_length

    return blocks


def find_free_spans(blocks: list) -> list:
    """
    Scan 'blocks' and return a list of tuples (start_index, span_length)
    for each contiguous region of free space ('.') in the disk.
    """
    free_spans = []
    start = None

    for i, b in enumerate(blocks):
        if b == ".":
            if start is None:
                start = i
        else:
            if start is not None:
                # We reached the end of a free span
                free_spans.append((start, i - start))
                start = None

    # If the disk ends with free space
    if start is not None:
        free_spans.append((start, len(blocks) - start))

    return free_spans


def move_file_whole(blocks: list, file_id: int) -> None:
    """
    Attempt to move the entire file with 'file_id' to the leftmost free-space span
    that can accommodate it, if such a span exists to the *left* of the file’s current position.
    Modifies 'blocks' in place. If no valid free span is found, the file does not move.
    """
    # Identify the indices occupied by this file
    file_indices = [i for i, val in enumerate(blocks) if val == file_id]
    if not file_indices:
        return  # File not found (possibly length 0 in dense map)

    # The file occupies contiguous or possibly multiple contiguous segments,
    # but in the original problem each file is initially contiguous. We’ll handle it generally:
    file_length = len(file_indices)
    current_leftmost_file_index = min(file_indices)

    # Find all contiguous free spans
    free_spans = find_free_spans(blocks)

    # We only consider free spans that start to the left of the leftmost file block index
    # (the puzzle states: "If there is no span of free space to the left of a file that is large enough to fit the file, the file does not move.")
    # But the example also sometimes shows a file skipping over large free segments between files.
    #
    # The puzzle states: "Attempt to move whole files to the leftmost span of free space blocks that could fit the file."
    # It doesn't explicitly say the free space must be strictly left of the file's *starting position*,
    # just to the left somewhere on the disk. But the example shows it effectively moves the file to the earliest left gap it can fill.
    #
    # We'll interpret the puzzle literally: we search for free spans anywhere to the left in the list,
    # as long as its start < current_leftmost_file_index.
    # Because if a big free span is partially or wholly left of the file, we can move the file there.
    #
    # If the puzzle's text means "strictly left (lower index) of *all* blocks of the file,"
    # then we require the free span to end at or before current_leftmost_file_index.
    # But in the puzzle’s example, the newly placed file can end up overlapping the original location
    # if the free space is partially overlapping.
    #
    # For clarity, let's match the example: we want the leftmost possible free span.
    # We'll simply find the free span that is as far left as possible,
    # big enough to hold the file, with start < current_leftmost_file_index.
    # If none is found, we do nothing.

    candidates = []
    for start_idx, span_len in free_spans:
        if start_idx + span_len <= current_leftmost_file_index:
            # Entire free span is strictly to the left of the file
            if span_len >= file_length:
                candidates.append((start_idx, span_len))

    # If no valid free span is found, do not move the file
    if not candidates:
        return

    # Among all valid candidates, pick the leftmost
    # (lowest 'start_idx')
    best_span = min(candidates, key=lambda x: x[0])
    (free_start, free_length) = best_span

    # Move the file blocks into that free span
    # 1. Sort file_indices so we can move in ascending order
    file_indices.sort()

    # 2. We place the file contiguously starting at free_start
    for offset, idx in enumerate(file_indices):
        # Move block from idx to (free_start + offset)
        blocks[free_start + offset] = file_id

    # 3. The old file positions become free
    for old_idx in file_indices:
        blocks[old_idx] = "."


def compact_disk_whole_files(blocks: list) -> None:
    """
    Perform the new compaction strategy:
      - Identify all file IDs present.
      - Move each file exactly once, in order of decreasing file ID number.
      - Only move the file if there is a leftmost free span large enough to contain it fully.
      - If not, the file does not move.
    """
    # Figure out what file IDs exist
    file_ids = sorted({val for val in blocks if val != "."})

    # Move in decreasing order
    for fid in reversed(file_ids):
        move_file_whole(blocks, fid)


def compute_checksum(blocks: list) -> int:
    """
    Given a list of blocks (where integers represent file IDs and '.' is free space),
    return the sum of (position * file_id) for all file blocks.
    """
    checksum = 0
    for pos, val in enumerate(blocks):
        if val != ".":
            checksum += pos * val
    return checksum


def main():
    # Example puzzle input from the previous step, which was also used here:
    with open("input.txt", "r", encoding="utf-8") as f:
        puzzle_input = f.read().strip()

    # 1. Parse the disk map to get the list of blocks
    blocks = parse_disk_map(puzzle_input)

    # 2. Compact using the *whole-file* approach
    compact_disk_whole_files(blocks)

    # 3. Compute checksum
    result = compute_checksum(blocks)

    print("Final checksum using whole-file compaction:", result)


if __name__ == "__main__":
    main()

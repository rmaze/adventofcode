use std::fs;

fn main() {
    let input = fs::read_to_string("src/day02/input.txt")
        .expect("Failed to read input file");
    let result = solve(&input);
    println!("Part 2: {}", result);
}

fn solve(input: &str) -> i32 {
    // TODO: Implement Day 2, Part 2
    input.lines().count() as i32
}

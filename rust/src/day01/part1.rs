use std::fs;

fn main() {
    let input = fs::read_to_string("src/day01/input.txt")
        .expect("Failed to read input file");
    let result = solve(&input);
    println!("Part 1: {}", result);
}

fn solve(input: &str) -> i32 {
    // TODO: Implement Day 1, Part 1
    input.lines().count() as i32
}

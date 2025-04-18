use aoc_2024::{is_safe_with_dampener, solve_day_02};
use std::fs;

fn main() {
    let input = fs::read_to_string("src/day02/input.txt").expect("Failed to read input file");
    let result = solve_day_02(&input, is_safe_with_dampener);
    println!("Part 2 Day 2: {}", result);
}

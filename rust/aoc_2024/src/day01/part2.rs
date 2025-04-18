use aoc_2024::similarity_score;
use std::fs;

fn main() {
    let input = fs::read_to_string("src/day01/input.txt").expect("Failed to read input file");
    let result = similarity_score(&input);
    println!("Part 2 Day 1: {}", result);
}

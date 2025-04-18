use aoc_2024::total_sorted_distance;
use std::fs;

fn main() {
    let input = fs::read_to_string("src/day01/input.txt").expect("Failed to read input file");
    let result = total_sorted_distance(&input);
    println!("Part 1 Day 1: {}", result);
}

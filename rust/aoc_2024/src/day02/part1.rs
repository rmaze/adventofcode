use aoc_2024::is_safe_report;
use std::fs;

fn main() {
    let input = fs::read_to_string("src/day02/input.txt").expect("Failed to read input file");
    let result = solve(&input);
    println!("Part 1: {}", result);
}

fn solve(input: &str) -> i32 {
    input
        .lines()
        .map(|line| {
            let levels: Vec<i32> = line
                .split_whitespace()
                .map(|s| s.parse::<i32>().unwrap())
                .collect();
            is_safe_report(&levels) as i32
        })
        .sum()
}

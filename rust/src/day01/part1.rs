use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() {
    let result = solve("src/day01/input.txt").expect("Failed to process input");
    println!("Part 1: {}", result);
}

fn solve(path: &str) -> io::Result<i32> {
    let file = File::open(path)?;
    let reader = BufReader::new(file);

    let mut left_list = Vec::new();
    let mut right_list = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let mut parts = line.split_whitespace();

        let left_val: i32 = parts.next().unwrap().parse().unwrap();
        let right_val: i32 = parts.next().unwrap().parse().unwrap();

        left_list.push(left_val);
        right_list.push(right_val);
    }

    left_list.sort();
    right_list.sort();

    let total_distance: i32 = left_list
        .iter()
        .zip(right_list.iter())
        .map(|(l, r)| (l - r).abs())
        .sum();

    Ok(total_distance)
}

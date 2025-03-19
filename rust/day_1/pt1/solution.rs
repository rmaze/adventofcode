use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let lines: Vec<String> = stdin.lock().lines().filter_map(Result::ok).collect();

    let mut left_list = Vec::new();
    let mut right_list = Vec::new();

    for (idx, line) in lines.iter().enumerate() {
        let parts: Vec<&str> = line.split_whitespace().collect();
        if parts.len() != 2 {
            panic!("Invalid input at line {}", idx + 1);
        }
        let left_val: i32 = parts[0].parse().expect("Invalid integer");
        let right_val: i32 = parts[1].parse().expect("Invalid integer");
        left_list.push(left_val);
        right_list.push(right_val);
    }

    left_list.sort();
    right_list.sort();

    let total_distance: i32 = left_list.iter()
        .zip(right_list.iter())
        .map(|(l, r)| (l - r).abs())
        .sum();

    println!("{}", total_distance);
}
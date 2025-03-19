use std::collections::HashMap;
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut left_list = Vec::new();
    let mut right_list = Vec::new();

    for line in stdin.lock().lines().flatten() {
        let mut nums = line.split_whitespace();
        left_list.push(nums.next().unwrap().parse::<i32>().unwrap());
        right_list.push(nums.next().unwrap().parse::<i32>().unwrap());
    }

    let mut right_counts = HashMap::new();
    for &num in &right_list {
        *right_counts.entry(num).or_insert(0) += 1;
    }

    let mut similarity_score = 0;
    for &num in &left_list {
        if let Some(&count) = right_counts.get(&num) {
            similarity_score += num * count;
        }
    }

    println!("{}", similarity_score);
}

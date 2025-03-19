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

    left_list.sort_unstable();
    right_list.sort_unstable();

    let mut total_distance = 0;
    for (l, r) in left_list.iter().zip(&right_list) {
        total_distance += (l - r).abs();
    }

    println!("{}", total_distance);
}

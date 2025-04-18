use std::collections::HashMap;
use std::fs;

fn main() {
    let input = fs::read_to_string("src/day01/input.txt").expect("Failed to read input file");
    let result = solve(&input);
    println!("Part 2: {}", result);
}

fn solve(input: &str) -> i32 {
    let mut left_list = Vec::new();
    let mut right_list = Vec::new();

    for line in input.lines() {
        let mut parts = line.split_whitespace();
        let l_val: i32 = parts.next().unwrap().parse().unwrap();
        let r_val: i32 = parts.next().unwrap().parse().unwrap();

        left_list.push(l_val);
        right_list.push(r_val);
    }

    let mut freq_right: HashMap<i32, i32> = HashMap::new();
    for val in right_list {
        *freq_right.entry(val).or_insert(0) += 1;
    }

    let similarity_score: i32 = left_list
        .iter()
        .map(|l| l * freq_right.get(l).unwrap_or(&0))
        .sum();

    similarity_score
}

use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let lines: Vec<String> = stdin.lock().lines().filter_map(Result::ok).collect();

    let mut left_list = Vec::with_capacity(lines.len());
    let mut right_list = Vec::with_capacity(lines.len());

    for (idx, line) in lines.iter().enumerate() {
        let mut parts = line.split_whitespace();
        let left_val: i32 = parts
            .next()
            .ok_or_else(|| format!("Missing left integer at line {}", idx + 1))
            .and_then(|v| {
                v.parse()
                    .map_err(|_| format!("Invalid left integer at line {}", idx + 1))
            })
            .expect("Parsing error");

        let right_val: i32 = parts
            .next()
            .ok_or_else(|| format!("Missing right integer at line {}", idx + 1))
            .and_then(|v| {
                v.parse()
                    .map_err(|_| format!("Invalid right integer at line {}", idx + 1))
            })
            .expect("Parsing error");

        left_list.push(left_val);
        right_list.push(right_val);
    }

    left_list.sort_unstable();
    right_list.sort_unstable();

    let total_distance: i32 = left_list
        .iter()
        .zip(right_list.iter())
        .map(|(l, r)| (l - r).abs())
        .sum();

    println!("{}", total_distance);
}

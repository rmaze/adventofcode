use std::collections::HashMap;

pub fn total_sorted_distance(input: &str) -> i32 {
    let mut left_list = Vec::new();
    let mut right_list = Vec::new();

    for line in input.lines() {
        let mut parts = line.split_whitespace();

        let left_val: i32 = parts.next().unwrap().parse().unwrap();
        let right_val: i32 = parts.next().unwrap().parse().unwrap();

        left_list.push(left_val);
        right_list.push(right_val);
    }

    left_list.sort();
    right_list.sort();

    left_list
        .iter()
        .zip(right_list.iter())
        .map(|(l, r)| (l - r).abs())
        .sum()
}
pub fn similarity_score(input: &str) -> i32 {
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

    left_list
        .iter()
        .map(|l| l * freq_right.get(l).unwrap_or(&0))
        .sum()
}

pub fn solve_day_02<F>(input: &str, predicate: F) -> i32
where
    F: Fn(&[i32]) -> bool,
{
    input
        .lines()
        .map(|line| {
            let levels: Vec<i32> = line
                .split_whitespace()
                .map(|s| s.parse::<i32>().unwrap())
                .collect();
            predicate(&levels) as i32
        })
        .sum()
}
pub fn is_strictly_safe(levels: &[i32]) -> bool {
    if levels.len() < 2 {
        return true;
    }

    let diffs: Vec<i32> = levels.windows(2).map(|pair| pair[1] - pair[0]).collect();

    for &d in &diffs {
        if d == 0 || d.abs() > 3 {
            return false;
        }
    }

    let all_positive = diffs.iter().all(|&d| d > 0);
    let all_negative = diffs.iter().all(|&d| d < 0);

    all_positive || all_negative
}
pub fn is_safe_report(levels: &[i32]) -> bool {
    if levels.len() < 2 {
        return false;
    }

    let diffs: Vec<i32> = levels.windows(2).map(|pair| pair[1] - pair[0]).collect();

    for &d in &diffs {
        if d == 0 || d.abs() < 1 || d.abs() > 3 {
            return false;
        }
    }

    let all_positive = diffs.iter().all(|&d| d > 0);
    let all_negative = diffs.iter().all(|&d| d < 0);

    all_positive || all_negative
}
pub fn is_safe_with_dampener(levels: &[i32]) -> bool {
    if is_strictly_safe(levels) {
        return true;
    }

    for i in 0..levels.len() {
        let mut modified = Vec::with_capacity(levels.len() - 1);
        modified.extend_from_slice(&levels[..i]);
        modified.extend_from_slice(&levels[i + 1..]);

        if is_strictly_safe(&modified) {
            return true;
        }
    }

    false
}

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

pub fn solve_day_02<F>(input: &str, predicate: F) -> u16
where
    F: Fn(&[u8]) -> bool,
{
    input
        .lines()
        .map(|line| {
            let levels: Vec<u8> = line
                .split_whitespace()
                .map(|s| s.parse::<u8>().unwrap())
                .collect();
            predicate(&levels) as u16
        })
        .sum()
}
pub fn is_strictly_safe(levels: &[u8]) -> bool {
    if levels.len() < 2 {
        return true;
    }

    let mut first_diff: Option<i16> = None;

    for pair in levels.windows(2) {
        let diff = pair[1] as i16 - pair[0] as i16;

        if diff == 0 || diff.abs() > 3 {
            return false;
        }

        match first_diff {
            None => first_diff = Some(diff.signum()),
            Some(sign) if diff.signum() != sign => return false,
            _ => {}
        }
    }

    true
}
pub fn is_safe_report(levels: &[u8]) -> bool {
    if levels.len() < 2 {
        return false;
    }

    let mut first_diff: Option<i16> = None;

    for pair in levels.windows(2) {
        let diff = pair[1] as i16 - pair[0] as i16;

        if diff == 0 || diff.abs() < 1 || diff.abs() > 3 {
            return false;
        }

        match first_diff {
            None => first_diff = Some(diff.signum()),
            Some(sign) if diff.signum() != sign => return false,
            _ => {}
        }
    }

    true
}
pub fn is_safe_with_dampener(levels: &[u8]) -> bool {
    if is_strictly_safe(levels) {
        return true;
    }

    for i in 0..levels.len() {
        let mut prev: Option<u8> = None;
        let mut valid = true;
        let mut first_diff: Option<i16> = None;

        for (j, &val) in levels.iter().enumerate() {
            if j == i {
                continue;
            }

            if let Some(p) = prev {
                let diff = val as i16 - p as i16;

                if diff == 0 || diff.abs() > 3 {
                    valid = false;
                    break;
                }

                match first_diff {
                    None => first_diff = Some(diff.signum()),
                    Some(sign) if diff.signum() != sign => {
                        valid = false;
                        break;
                    }
                    _ => {}
                }
            }

            prev = Some(val);
        }

        if valid {
            return true;
        }
    }

    false
}

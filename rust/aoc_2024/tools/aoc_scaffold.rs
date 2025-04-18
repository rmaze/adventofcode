use std::fs;
use std::path::Path;

fn main() {
    for day in 1..=25 {
        let dir = format!("src/day{:02}", day);
        let part1 = format!("{}/part1.rs", &dir);
        let part2 = format!("{}/part2.rs", &dir);
        let input = format!("{}/input.txt", &dir);

        fs::create_dir_all(&dir).expect("Could not create day directory");

        create_file(&part1, &template("Part 1", day, 1));
        create_file(&part2, &template("Part 2", day, 2));
        create_file(&input, "");
    }

    println!("\n✅ Scaffolded all 25 Advent of Code days.");
}

fn create_file(path: &str, content: &str) {
    if Path::new(path).exists() {
        println!("  ⚠ Skipped existing file: {}", path);
    } else {
        fs::write(path, content).expect("Failed to write file");
        println!("  ✅ Created {}", path);
    }
}

fn template(label: &str, day: u8, part: u8) -> String {
    let day_str = format!("day{:02}", day);
    format!(
        r#"use std::fs;

fn main() {{
    let input = fs::read_to_string("src/{}/input.txt")
        .expect("Failed to read input file");
    let result = solve(&input);
    println!("{}: {{}}", result);
}}

fn solve(input: &str) -> i32 {{
    // TODO: Implement Day {}, Part {}
    input.lines().count() as i32
}}
"#,
        day_str, label, day, part
    )
}

use std::fs;

fn main() {
    let cargo_path = "Cargo.toml";
    let original = fs::read_to_string(cargo_path).expect("Failed to read Cargo.toml");

    let begin = "# BEGIN AOC BINS";
    let end = "# END AOC BINS";

    let new_bins = generate_bin_entries();

    let updated = if original.contains(begin) && original.contains(end) {
        // Replace existing section
        let start = original.find(begin).unwrap();
        let finish = original.find(end).unwrap() + end.len();
        format!(
            "{}{}\n{}",
            &original[..start],
            new_bins,
            &original[finish..]
        )
    } else {
        // Append section
        format!("{}\n\n{}\n", original.trim_end(), new_bins)
    };

    fs::write(cargo_path, updated).expect("Failed to write updated Cargo.toml");
    println!("✅ Cargo.toml updated with 48 binary entries.");
}

fn generate_bin_entries() -> String {
    let mut output = String::from("# BEGIN AOC BINS");
    for day in 1..=25 {
        for part in 1..=2 {
            let name = format!("day{:02}_part{}", day, part);
            let path = format!("src/day{:02}/part{}.rs", day, part);
            output.push_str(&format!(
                r#"

[[bin]]
name = "{}"
path = "{}"
"#,
                name, path
            ));
        }
    }
    output.push_str("\n# END AOC BINS");
    output
}

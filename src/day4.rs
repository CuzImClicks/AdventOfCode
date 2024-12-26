pub fn part1(input: Vec<&str>) -> anyhow::Result<usize> {
    let len = input[0].len();
    let mut total = 0;
    let mut all: String = String::new();
    input.into_iter().for_each(|line| all.push_str(line));
    println!("{}", &all);

    for i in 0..all.len() - 3 {
        if i % len < (i + 3) % len {
            let slice = &all[i..=i + 3];
            if slice == "XMAS" || slice == "SAMX" {
                total += 1;
            }
        }
        if i + 1 + 3 * len <= all.len() {
            let first: &str = &all[i..i + 1];
            let second = &all[i + len .. i + len + 1];
            let third = &all[i + 2 * len .. i + 2 * len + 1];
            let fourth = &all[i + 3 * len..i + 3 * len + 1];
            if (first == "X" && second == "M" && third == "A" && fourth == "S")
                || (first == "S" && second == "A" && third == "M" && fourth == "X") {
                total += 1;
            }
        }
        if i + 4 + 3 * len <= all.len() && (i % len < (i + 3) % len) {
            let first = &all[i..i + 1];
            let second = &all[i + 1 + len..i + 2 + len];
            let third = &all[i + 2 + 2 * len..i + 3 + 2 * len];
            let fourth = &all[i + 3 + 3 * len..i + 4 + 3 * len];
            if (first == "X" && second == "M" && third == "A" && fourth == "S")
                || (first == "S" && second == "A" && third == "M" && fourth == "X") {
                total += 1;
            }
        }
        if i - 2 + 3 * len <= all.len() && (i % len > (i - 3) % len) {
            let first: &str = &all[i..i + 1];
            let second = &all[i - 1 + len..i + len];
            let third = &all[i - 2 + 2 * len..i - 1 + 2 * len];
            let fourth = &all[i - 3 + 3 * len..i - 2 + 3 * len];
            if (first == "X" && second == "M" && third == "A" && fourth == "S")
                || (first == "S" && second == "A" && third == "M" && fourth == "X") {
                total += 1;
            }
        }
    }

    Ok(total)
}

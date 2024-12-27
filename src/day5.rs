pub fn part1(input: String) -> anyhow::Result<usize> {
    let mut total = 0;
    let input: Vec<&str> = input.split("\n\r\n").collect();
    let rules: Vec<&str> = input[0].lines().collect();
    let rules: Vec<(u8, u8)> = rules
        .into_iter()
        .filter(|it| !it.is_empty())
        .map(|l| {
            (
                l[0..2].parse::<u8>().unwrap(),
                l[3..5].parse::<u8>().unwrap(),
            )
        })
        .collect();
    for update in input[1].lines() {
        let mut valid = true;
        let update: Vec<u8> = update
            .split(",")
            .map(|it| it.parse::<u8>().unwrap())
            .collect();
        for (first, second) in rules.iter() {
            let pos = update.iter().position(|&x| x == *first);
            let pos2 = update.iter().position(|&x| x == *second);
            valid = match (pos, pos2) {
                (Some(p), Some(p2)) => p < p2,
                _ => true
            };
            
            if !valid {
                break;
            }
        }
        if valid {
            total += update[update.len() / 2] as usize;
        }
    }

    Ok(total)
}

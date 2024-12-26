

pub fn part1(mut input: Vec<&str>) -> anyhow::Result<usize> {
    
    let mut total: usize = 0;
    let xmas: &[char; 4] = &['X', 'M', 'A', 'S'];
    let mut smax: [char; 4] = xmas.clone(); 
    smax.reverse();
    let smax = &smax;
    
    for line in &input {
        let chars: Vec<char> = line.chars().collect();
        for i in 0..(chars.len() - 3) {
            let three_chars = &chars[i..=i+3];
            if three_chars ==  xmas || three_chars == smax {
                total += 1;
            }
        }
    }
    
    let rotated: Vec<String> = input.iter().map(|line| {
        let chars: Vec<char> = line.chars().collect();
        let mut rotated: Vec<char> = vec![];
        for i in 0..chars.len() {
            rotated.push(chars[(i + 1) % chars.len()]);
        }
        rotated.iter().collect::<String>()
    }).collect();
    
    for line in &rotated {
        let chars: Vec<char> = line.chars().collect();
        for i in 0..(chars.len() - 3) {
            let three_chars = &chars[i..=i+3];
            if three_chars ==  xmas || three_chars == smax {
                total += 1;
            }
        }
    }

    Ok(total)
}
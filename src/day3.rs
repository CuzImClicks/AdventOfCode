use anyhow::Result;



pub fn part1(input: String) -> Result<usize> {
    let mut index = 0;
    let mut total = 0;
    let mut first_num = String::new();
    let mut second_num = String::new();
    for char in input.chars() {
        if char == 'm' && index == 0 {
            index = 1;
        } else if char == 'u' && index == 1 {
            index = 2;
        } else if char == 'l' && index == 2 {
            index = 3;
        } else if char == '(' && index == 3 {
            index = 4;
        } else if char.is_numeric() && index == 4 {
            first_num.push(char);
        } else if char == ',' && index == 4 {
            index = 5;
        } else if char.is_numeric() && index == 5 {
            second_num.push(char);
        } else if char == ')' && index == 5 {
            total += first_num.parse::<usize>()? * second_num.parse::<usize>()?;
            first_num = String::new();
            second_num = String::new();
            index = 0;
        } else {
            first_num = String::new();
            second_num = String::new();
            index = 0;
        }
    }
    
    Ok(total)
}

pub fn part1(content: Vec<&str>) -> anyhow::Result<usize> {
    
    let input: Vec<Vec<u8>> = content.iter().map(|it| it.split(" ").map(|num| num.parse::<u8>().unwrap()).collect::<Vec<u8>>()).collect();

    let safe = input
        .iter()
        .map(|report| {
            let diffs = (*report)
                .windows(2)
                .all(|window| (1u8..=3u8).contains(&window[0].abs_diff(window[1])));
                
            let asc = (*report)
                .windows(2)
                .all(|window| window[0] < window[1]);
                
            let desc = (*report)
                .windows(2)
                .all(|window| window[0] > window[1]);
            diffs && (asc || desc)
    }).collect::<Vec<bool>>();
    
    Ok(safe.iter().filter(|it| **it).collect::<Vec<&bool>>().len())
}

fn check_desc(v: &Vec<u8>) -> bool {
    v.windows(2).all(|window| window[0] > window[1])
}

fn check_asc(v: &Vec<u8>) -> bool {
    v.windows(2).all(|window| window[0] < window[1])
}

pub fn part2(content: Vec<&str>) -> anyhow::Result<usize> {
    unimplemented!()
    //let input: Vec<Vec<u8>> = content.iter().map(|it| it.split(" ").map(|num| num.parse::<u8>().unwrap()).collect::<Vec<u8>>()).collect();
    //let mut second: Vec<Vec<u8>> = vec![];
    //
    //for mut report in input.into_iter() {
    //    for i in 1..report.len() -1 {
    //        let diff: u8 = report[i].abs_diff(report[i+1]);
    //        if diff > 3u8 || diff < 1u8 {
    //            report.remove(i+1);
    //            second.push(report);
    //            break;
    //        } else if report[i] < report 
    //    }
    //}

    //Ok(1)
    //Ok(safe.iter().filter(|it| **it).collect::<Vec<&bool>>().len())
}
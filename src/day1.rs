use std::fs;
use std::path::{PathBuf};

pub fn part1(path: PathBuf) -> anyhow::Result<usize> {
    let input: String = fs::read_to_string(path)?;
    let input: Vec<&str> = input.lines().collect();
    let input = input.iter().map(|it| it.split("   "));
    let mut left: Vec<usize> = Vec::with_capacity(1000);
    let mut right: Vec<usize> = Vec::with_capacity(1000);
    
    input.for_each(|mut it| {
        left.push_within_capacity(it.next().unwrap().parse::<usize>().unwrap()).unwrap();
        right.push_within_capacity(it.next().unwrap().parse::<usize>().unwrap()).unwrap();
    });
    
    left.sort();
    right.sort();
    let total: usize = left.iter().zip(right).map(|(left, right)| {
        left.abs_diff(right)
    }).sum();
    Ok(total)
}

pub fn part2(path: PathBuf) -> anyhow::Result<usize> {
    let input: String = fs::read_to_string(path)?;
    let input: Vec<&str> = input.lines().collect();
    let input = input.iter().map(|it| it.split("   "));
    let mut left: Vec<usize> = Vec::with_capacity(1000);
    let mut right: Vec<usize> = Vec::with_capacity(1000);

    input.for_each(|mut it| {
        left.push_within_capacity(it.next().unwrap().parse::<usize>().unwrap()).unwrap();
        right.push_within_capacity(it.next().unwrap().parse::<usize>().unwrap()).unwrap();
    });
    
    Ok(left.iter().map(|it| {
        it * right.iter().filter(|r| it == *r).collect::<Vec<&usize>>().len()
    }).sum())
}
#![feature(vec_push_within_capacity)]

use std::{fs, path::PathBuf};
use anyhow::Context;
use crate::inputs::get_input;

mod inputs;
mod day1;
mod day2;
mod day3;
mod day4;
mod day5;

fn main() -> anyhow::Result<()> {
    
    let day = std::env::args().nth(1).context("No day provided")?;
    let day: u8 = day.parse()?;
    let part = std::env::args().nth(2).context("No day provided")?;
    let part: u8 = part.parse()?;
    let path = std::env::args().nth(3).context("No day provided")?;
    let path = PathBuf::from(path);
    
    match day {
        1 => {
            if part == 1u8 {
                println!("{}", day1::part1(path)?);
            } else if part == 2u8 {
                println!("{}", day1::part2(path)?);
            }
        }
        2 => {
            if part == 1u8 {
                let content = get_input(path)?;
                println!("{}", day2::part1(content.lines().collect())?);
            } else if part == 2u8 {
                let content = get_input(path)?;
                println!("{}", day2::part2(content.lines().collect())?);
            }
        }
        3 => {
            if part == 1u8 {
                let content = get_input(path)?;
                println!("{}", day3::part1(content)?);
            }
        }
        4 => {
            if part == 1u8 {
                let content = get_input(path)?;
                println!("{}", day4::part1(content.lines().collect())?);
            } else if part == 2u8 {
                let content = get_input(path)?;
                println!("{}", day4::part2(content.lines().collect())?);
            }
        }
        5 => {
            if part == 1u8 {
                let content = fs::read_to_string(path)?;
                println!("{}", day5::part1(content)?);
            }
        }
        _ => {
            unimplemented!()
        }
    }
    
    Ok(())
}

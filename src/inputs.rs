use std::{fs, io};
use std::path::{Path};
use anyhow::Context;

pub fn get_input<P: AsRef<Path>>(path: P) -> anyhow::Result<String> {
    fs::read_to_string(path.as_ref()).context("Failed to read puzzle input")
}

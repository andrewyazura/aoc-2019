[![SWUbanner](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md)

# 🎄 Advent of Code 2019 🎄

Advent of Code 2019 solutions on Python

[Official Advent of Code page](https://adventofcode.com/2019)

## Setup

Set `PYTHONPATH` before to be able to run solutions that use `amplifier.py` and `intcode_compiler.py`.

Example: `export PYTHONPATH=/path/to/project/root`

## For those who solve

### Day 7

I had many troubles with part 2. I spent many hours debugging it line by line just to find out this:

- I forgot to comment out part 1, so I was debugging wrong code
- In part 2, you should stop the execution when ALL computers halted. At first I checked if any of them did and this was my main mistake.

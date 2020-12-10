import math

puzzle_input = []

with open('day-1/input.txt', 'r') as file:
    puzzle_input = [int(i.strip()) for i in file.readlines()]


def calculate_fuel(module_mass):
    return math.floor(module_mass / 3) - 2


def part_1(puzzle_input):
    result = 0

    for entry in puzzle_input:
        result += calculate_fuel(entry)

    return result


def part_2(puzzle_input):
    result = 0

    for entry in puzzle_input:
        fuel = calculate_fuel(entry)
        last_fuel = fuel

        while calculate_fuel(last_fuel) > 0:
            fuel += calculate_fuel(last_fuel)
            last_fuel = calculate_fuel(last_fuel)

        result += fuel

    return result


print(part_1(puzzle_input))
print(part_2(puzzle_input))

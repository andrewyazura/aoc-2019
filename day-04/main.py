puzzle_input = '156218-652527'


def is_ascending(num):
    last_digit = 0
    for digit in map(int, str(num)):
        if digit < last_digit:
            return False

        last_digit = digit

    return True


def part_1(puzzle_input):
    start, stop = puzzle_input.split('-')
    start = int(start)
    stop = int(stop)

    valid = 0

    for password in range(start, stop):
        password_str = str(password)
        repeats = []

        for digit in map(int, password_str):
            repeats.append(
                password_str.count(
                    str(digit)
                )
            )

        doubles = list(filter(lambda x: x >= 2, repeats))

        if doubles and is_ascending(password):
            valid += 1

    return valid


def part_2(puzzle_input):
    start, stop = puzzle_input.split('-')
    start = int(start)
    stop = int(stop)

    valid = 0

    for password in range(start, stop):
        password_str = str(password)
        repeats = []

        for digit in map(int, password_str):
            repeats.append(
                password_str.count(
                    str(digit)
                )
            )

        if 2 in repeats and is_ascending(password):
            valid += 1

    return valid


print(part_1(puzzle_input))
print(part_2(puzzle_input))

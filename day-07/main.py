import itertools

from amplifier import Amplifier, one_amplifier_running

puzzle_input = []

with open('day-7/input.txt', 'r') as file:
    puzzle_input = [int(i.strip()) for i in file.read().split(',')]


def part_1(puzzle_input):
    permutations = list(itertools.permutations(range(0, 5), 5))
    highest_output = 0

    for option in permutations:
        amplifiers = []
        for i in range(5):
            amp = Amplifier(puzzle_input)
            amp.append_input(option[i])
            amplifiers.append(amp)

        for i in range(4):
            amplifiers[i].set_next(
                amplifiers[i + 1]
            )

        amplifiers[0].append_input(0)
        for amp in amplifiers:
            amp.execute()

        highest_output = max(
            highest_output,
            *amplifiers[-1].saved_output
        )

    return highest_output


def part_2(puzzle_input):
    permutations = list(itertools.permutations(range(5, 10), 5))
    highest_output = 0

    for option in permutations:
        amplifiers = []
        for i in range(5):
            amp = Amplifier(puzzle_input)
            amp.append_input(option[i])
            amplifiers.append(amp)

        for i in range(5):
            amplifiers[i].set_next(
                amplifiers[(i + 1) % 5]
            )
        amplifiers[0].append_input(0)

        i = 0
        while one_amplifier_running(amplifiers):
            amplifiers[i].execute()
            i = (i + 1) % 5

        highest_output = max(
            highest_output,
            *amplifiers[-1].saved_output
        )

    return highest_output


print(part_1(puzzle_input))
print(part_2(puzzle_input))

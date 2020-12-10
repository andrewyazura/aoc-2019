from intcode_interpreter import IntcodeInterpreter

puzzle_input = []

with open('day-5/input.txt', 'r') as file:
    puzzle_input = [int(i.strip()) for i in file.read().split(',')]


def part_1(puzzle_input):
    puzzle = puzzle_input.copy()
    interpreter = IntcodeInterpreter(puzzle)
    interpreter.set_input(1)
    interpreter.execute()
    return interpreter.saved_output[-1]


def part_2(puzzle_input):
    puzzle = puzzle_input.copy()
    interpreter = IntcodeInterpreter(puzzle)
    interpreter.set_input(5)
    interpreter.execute()
    return interpreter.saved_output[-1]


print(part_1(puzzle_input))
print(part_2(puzzle_input))

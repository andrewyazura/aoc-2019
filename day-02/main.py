import itertools

puzzle_input = []

with open('day-2/input.txt', 'r') as file:
    puzzle_input = [int(i.strip()) for i in file.read().split(',')]


class IntcodeInterpreter:
    def __init__(self, memory):
        self.memory = memory
        self.opcodes = {
            1: self.add,
            2: self.multiply
        }

    def add(self, addr1, addr2, addr3):
        self.memory[addr3] = self.memory[addr1] + self.memory[addr2]
        return self.memory[addr3]

    def multiply(self, addr1, addr2, addr3):
        self.memory[addr3] = self.memory[addr1] * self.memory[addr2]
        return self.memory[addr3]

    def execute(self):
        pointer = 0

        while pointer <= len(self.memory):
            opcode = self.memory[pointer]

            if opcode == 99:
                return self.memory

            self.opcodes[opcode](*[self.memory[pointer + i]
                                   for i in range(1, 4)])
            pointer += 4


def part_1(puzzle_input):
    puzzle = puzzle_input.copy()

    puzzle[1] = 12
    puzzle[2] = 2

    interpreter = IntcodeInterpreter(puzzle)
    return interpreter.execute()[0]


def part_2(puzzle_input):
    for pair in itertools.product(range(0, 100), range(0, 100)):
        puzzle = puzzle_input.copy()

        noun = pair[0]
        verb = pair[1]

        puzzle[1] = noun
        puzzle[2] = verb

        interpreter = IntcodeInterpreter(puzzle)
        result = interpreter.execute()[0]

        if result == 19690720:
            return 100 * noun + verb


print(part_1(puzzle_input))
print(part_2(puzzle_input))

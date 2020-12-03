puzzle_input = []

with open('day-5/input.txt', 'r') as file:
    puzzle_input = [int(i.strip()) for i in file.read().split(',')]


class IntcodeInterpreter:
    def __init__(self, memory):
        self.memory = memory
        self.preset_input = []
        self.saved_output = []
        self.pointer = 0
        self.opcodes = {
            1: {
                'func': self.sum,
                'shift': 4
            },
            2: {
                'func': self.multiply,
                'shift': 4
            },
            3: {
                'func': self.input,
                'shift': 2
            },
            4: {
                'func': self.output,
                'shift': 2
            },
            5: {
                'func': self.jump_if_true,
                'shift': 3
            },
            6: {
                'func': self.jump_if_false,
                'shift': 3
            },
            7: {
                'func': self.less_than,
                'shift': 4
            },
            8: {
                'func': self.equals,
                'shift': 4
            },
        }

    def provide_input(self, *args):
        self.preset_input.extend(args)

    def interpret_instruction(self, instruction):
        instruction = str(instruction).rjust(5, ' ')
        opcode = int(instruction[3:])
        modes = [int(x) if x != ' ' else 0 for x in instruction[2::-1]]

        return opcode, modes

    def sum(self, addr1, addr2, addr3):
        self.memory[addr3] = self.memory[addr1] + self.memory[addr2]
        return self.memory[addr3]

    def multiply(self, addr1, addr2, addr3):
        self.memory[addr3] = self.memory[addr1] * self.memory[addr2]
        return self.memory[addr3]

    def input(self, addr):
        self.memory[addr] = self.preset_input.pop(0) \
            if self.preset_input else self._input()
        return self.memory[addr]

    def _input(self):
        answer = None

        while answer is None:
            try:
                answer = int(input('enter value: '))
            except:
                answer = None

        return answer

    def output(self, addr):
        r = self.memory[addr]
        self.saved_output.append(r)
        return r

    def jump_if_true(self, addr1, addr2):
        if self.memory[addr1] != 0:
            self.pointer = self.memory[addr2]
            return

        return self.pointer

    def jump_if_false(self, addr1, addr2):
        if self.memory[addr1] == 0:
            self.pointer = self.memory[addr2]
            return

        return self.pointer

    def less_than(self, addr1, addr2, addr3):
        result = int(self.memory[addr1] < self.memory[addr2])
        self.memory[addr3] = result
        return result

    def equals(self, addr1, addr2, addr3):
        result = int(self.memory[addr1] == self.memory[addr2])
        self.memory[addr3] = result
        return result

    def execute(self):
        while self.pointer <= len(self.memory):
            instruction = self.memory[self.pointer]
            opcode, modes = self.interpret_instruction(
                instruction
            )

            if opcode == 99:
                return self.memory, self.saved_output

            opcode_func = self.opcodes[opcode]['func']
            opcode_shift = self.opcodes[opcode]['shift']
            params = []

            for i in range(1, opcode_shift):
                if modes[i - 1] == 0:
                    params.append(self.memory[self.pointer + i])

                elif modes[i - 1] == 1:
                    params.append(self.pointer + i)

            result = opcode_func(*params)
            self.pointer += opcode_shift if result is not None else 0


def part_1(puzzle_input):
    puzzle = puzzle_input.copy()
    interpreter = IntcodeInterpreter(puzzle)
    interpreter.provide_input(1)
    return interpreter.execute()[1][-1]


def part_2(puzzle_input):
    puzzle = puzzle_input.copy()
    interpreter = IntcodeInterpreter(puzzle)
    interpreter.provide_input(5)
    return interpreter.execute()[1][-1]


print(part_1(puzzle_input))
print(part_2(puzzle_input))

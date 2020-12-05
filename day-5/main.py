puzzle_input = []

with open('day-5/input.txt', 'r') as file:
    puzzle_input = [int(i.strip()) for i in file.read().split(',')]


class InputException(Exception):
    pass


class IntcodeInterpreter:
    def __init__(self, memory):
        self.running = True
        self.memory = memory.copy()
        self.pointer = 0

        self.saved_input = None
        self.saved_output = []

        self.opcodes = {
            1: {
                'func': self._add,
                'shift': 4
            },
            2: {
                'func': self._multiply,
                'shift': 4
            },
            3: {
                'func': self._get_input,
                'shift': 2
            },
            4: {
                'func': self._send_output,
                'shift': 2
            },
            5: {
                'func': self._jump_if_true,
                'shift': 3
            },
            6: {
                'func': self._jump_if_false,
                'shift': 3
            },
            7: {
                'func': self._less_than,
                'shift': 4
            },
            8: {
                'func': self._equals,
                'shift': 4
            },
            99: {
                'func': self._terminate,
                'shift': 0
            }
        }

    def _add(self, addr1, addr2, addr3):
        self.memory[addr3] = self.memory[addr1] + self.memory[addr2]
        self.pointer += 4

    def _multiply(self, addr1, addr2, addr3):
        self.memory[addr3] = self.memory[addr1] * self.memory[addr2]
        self.pointer += 4

    def _get_input(self, addr1):
        if self.saved_input is not None:
            self.memory[addr1] = self.saved_input
            self.saved_input = None

        else:
            raise InputException(
                f'self.saved_input is empty; pointer={self.pointer}')

        self.pointer += 2

    def _send_output(self, addr1):
        self.saved_output.append(self.memory[addr1])
        self.pointer += 2

    def _jump_if_true(self, addr1, addr2):
        if self.memory[addr1] != 0:
            self.pointer = self.memory[addr2]

        else:
            self.pointer += 3

    def _jump_if_false(self, addr1, addr2):
        if self.memory[addr1] == 0:
            self.pointer = self.memory[addr2]

        else:
            self.pointer += 3

    def _less_than(self, addr1, addr2, addr3):
        result = int(self.memory[addr1] < self.memory[addr2])
        self.memory[addr3] = result
        self.pointer += 4

    def _equals(self, addr1, addr2, addr3):
        result = int(self.memory[addr1] == self.memory[addr2])
        self.memory[addr3] = result
        self.pointer += 4

    def _terminate(self):
        self.running = False

    def execute(self):
        while self.running and self.pointer <= len(self.memory):
            instruction = self.memory[self.pointer]
            opcode, modes = self.interpret_instruction(
                instruction
            )

            opcode_func = self.opcodes[opcode]['func']
            opcode_shift = self.opcodes[opcode]['shift']
            params = []

            for i in range(1, opcode_shift):
                if modes[i - 1] == 0:
                    params.append(self.memory[self.pointer + i])

                elif modes[i - 1] == 1:
                    params.append(self.pointer + i)

            opcode_func(*params)

    def interpret_instruction(self, instruction):
        instruction = str(instruction).rjust(5, ' ')
        opcode = int(instruction[3:])
        modes = [int(x) if x != ' ' else 0 for x in instruction[2::-1]]

        return opcode, modes

    def set_input(self, value):
        self.saved_input = value


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

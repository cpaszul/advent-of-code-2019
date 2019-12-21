class Memory:
    def __init__(self, memory):
        self.memory = memory

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('memory addresses must be integers')
        if key < 0:
            raise IndexError('memory addresses cannot be negative')
        if key >= len(self.memory):
            self.memory += [0] * (key - len(self.memory) + 1)
        return self.memory[key]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError('memory addresses must be integers')
        if key < 0:
            raise IndexError('memory addresses cannot be negative')
        if key >= len(self.memory):
            self.memory += [0] * (key - len(self.memory) + 1)
        self.memory[key] = value


class IntCode:
    def __init__(self, memory, *inputs):
        self.memory = Memory(memory)
        self.inputs = list(inputs)
        self.pointer = 0
        self.offset = 0

    def get_input(self):
        if not self.inputs:
            raise AttributeError('IntCode has no input values')
        return self.inputs.pop(0)

    def add_inputs(self, *inputs):
        self.inputs += list(inputs)

    def add_ascii_inputs(self, string):
        if string[-1] != '\n':
            string += '\n'
        self.add_inputs(*(ord(ch) for ch in string))

    def get_output(self):
        while True:
            inst = self.memory[self.pointer]
            padded_inst = str(inst).zfill(5)
            third_mode, second_mode, first_mode, opcode = \
                        map(int, (padded_inst[0], padded_inst[1],
                                  padded_inst[2], padded_inst[3:]))
            if opcode == 99:
                return (True, 0)
            if opcode == 1:
                self.write(3, third_mode,
                           self.read(1, first_mode) + self.read(2, second_mode))
                self.pointer += 4
            if opcode == 2:
                self.write(3, third_mode,
                           self.read(1, first_mode) * self.read(2, second_mode))
                self.pointer += 4
            if opcode == 3:
                self.write(1, first_mode, self.get_input())
                self.pointer += 2
            if opcode == 4:
                output_value = self.read(1, first_mode)
                self.pointer += 2
                return (False, output_value)
            if opcode == 5:
                first_value = self.read(1, first_mode)
                if first_value != 0:
                    self.pointer = self.read(2, second_mode)
                else:
                    self.pointer += 3
            if opcode == 6:
                first_value = self.read(1, first_mode)
                if first_value == 0:
                    self.pointer = self.read(2, second_mode)
                else:
                    self.pointer += 3
            if opcode == 7:
                if self.read(1, first_mode) < self.read(2, second_mode):
                    self.write(3, third_mode, 1)
                else:
                    self.write(3, third_mode, 0)
                self.pointer += 4
            if opcode == 8:
                if self.read(1, first_mode) == self.read(2, second_mode):
                    self.write(3, third_mode, 1)
                else:
                    self.write(3, third_mode, 0)
                self.pointer += 4
            if opcode == 9:
                self.offset += self.read(1, first_mode)
                self.pointer += 2

    def run_through(self):
        outputs = []
        while not (output := self.get_output())[0]:
            outputs.append(output[1])
        return outputs

    def read(self, parameter, mode):
        if mode == 2:
            addr = self.memory[self.pointer + parameter] + self.offset
            return self.memory[addr]
        elif mode == 1:
            value = self.memory[self.pointer + parameter]
            return value
        elif mode == 0:
            addr = self.memory[self.pointer + parameter]
            return self.memory[addr]

    def write(self, parameter, mode, value):
        if mode == 2:
            addr = self.memory[self.pointer + parameter] + self.offset
            self.memory[addr] = value
        elif mode == 0:
            addr = self.memory[self.pointer + parameter]
            self.memory[addr] = value

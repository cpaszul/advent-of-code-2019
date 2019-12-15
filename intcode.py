class IntCode:
    def __init__(self, instructions, first_input=0, rest_input=None):
        self.instructions = instructions
        self.instructions += [0] * 10000
        self.first_input = first_input
        self.use_first_input = True
        if rest_input is None:
            self.rest_input = first_input
        else:
            self.rest_input = rest_input
        self.i = 0
        self.offset = 0

    def set_input(self, x):
        self.first_input = x
        self.rest_input = x

    def get_output(self):
        while True:
            inst = self.instructions[self.i]
            padded_inst = str(inst).zfill(5)
            third_mode, second_mode, first_mode, opcode = \
                        map(int, (padded_inst[0], padded_inst[1],
                                  padded_inst[2], padded_inst[3:]))
            if opcode == 99:
                return (True, 0)
            if opcode == 1:
                self.write(3, third_mode,
                           self.read(1, first_mode) + self.read(2, second_mode))
                self. i += 4
            if opcode == 2:
                self.write(3, third_mode,
                           self.read(1, first_mode) * self.read(2, second_mode))
                self.i += 4
            if opcode == 3:
                if self.use_first_input:
                    self.write(1, first_mode, self.first_input)
                    self.use_first_input = False
                else:
                    self.write(1, first_mode, self.rest_input)
                self.i += 2
            if opcode == 4:
                output_value = self.read(1, first_mode)
                self.i += 2
                return (False, output_value)
            if opcode == 5:
                first_value = self.read(1, first_mode)
                if first_value != 0:
                    self.i = self.read(2, second_mode)
                else:
                    self.i += 3
            if opcode == 6:
                first_value = self.read(1, first_mode)
                if first_value == 0:
                    self.i = self.read(2, second_mode)
                else:
                    self.i += 3
            if opcode == 7:
                if self.read(1, first_mode) < self.read(2, second_mode):
                    self.write(3, third_mode, 1)
                else:
                    self.write(3, third_mode, 0)
                self.i += 4
            if opcode == 8:
                if self.read(1, first_mode) == self.read(2, second_mode):
                    self.write(3, third_mode, 1)
                else:
                    self.write(3, third_mode, 0)
                self.i += 4
            if opcode == 9:
                self.offset += self.read(1, first_mode)
                self.i += 2

    def run_through(self):
        outputs = []
        while not (output := self.get_output())[0]:
            outputs.append(output[1])
        return outputs

    def read(self, parameter, mode):
        if mode == 2:
            addr = self.instructions[self.i + parameter] + self.offset
            return self.instructions[addr]
        elif mode == 1:
            value = self.instructions[self.i + parameter]
            return value
        elif mode == 0:
            addr = self.instructions[self.i + parameter]
            return self.instructions[addr]

    def write(self, parameter, mode, value):
        if mode == 2:
            addr = self.instructions[self.i + parameter] + self.offset
            self.instructions[addr] = value
        elif mode == 0:
            addr = self.instructions[self.i + parameter]
            self.instructions[addr] = value

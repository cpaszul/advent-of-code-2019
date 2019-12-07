class IntCode:
    def __init__(self, instructions, first_input=0, rest_input=None):
        self.instructions = instructions
        self.first_input = first_input
        self.use_first_input = True
        if rest_input is None:
            self.rest_input = first_input
        else:
            self.rest_input = rest_input
        self.i = 0

    def set_input(self, x):
        self.rest_input = x

    def get_output(self):
        while True:
            inst = self.instructions[self.i]
            padded_inst = str(inst).zfill(5)
            third_mode, second_mode, first_mode, opcode = \
                        map(int, (padded_inst[0], padded_inst[1],
                                  padded_inst[2], padded_inst[3:]))
            if opcode == 99:
                return True
            if opcode == 1:
                self._add(first_mode, second_mode)
            if opcode == 2:
                self._mult(first_mode, second_mode)
            if opcode == 3:
                self._write()
            if opcode == 4:
                return self._output(first_mode)
            if opcode == 5:
                self._jump_if_true(first_mode, second_mode)
            if opcode == 6:
                self._jump_if_false(first_mode, second_mode)
            if opcode == 7:
                self._less_than(first_mode, second_mode)
            if opcode == 8:
                self._equals(first_mode, second_mode)

    def run_through(self):
        outputs = []
        while True:
            next_output = self.get_output()
            if next_output is True:
                return outputs
            outputs.append(next_output)

    def _add(self, first_mode, second_mode):
        if first_mode == 1:
            first_value = self.instructions[self.i + 1]
        else:
            first_value = self.instructions[self.instructions[self.i + 1]]
        if second_mode == 1:
            second_value = self.instructions[self.i + 2]
        else:
            second_value = self.instructions[self.instructions[self.i + 2]]
        self.instructions[self.instructions[self.i + 3]] = \
                                                   first_value + second_value
        self.i += 4

    def _mult(self, first_mode, second_mode):
        if first_mode == 1:
            first_value = self.instructions[self.i + 1]
        else:
            first_value = self.instructions[self.instructions[self.i + 1]]
        if second_mode == 1:
            second_value = self.instructions[self.i + 2]
        else:
            second_value = self.instructions[self.instructions[self.i + 2]]
        self.instructions[self.instructions[self.i + 3]] = \
                                                   first_value * second_value
        self.i += 4

    def _write(self):
        if self.use_first_input:
            self.instructions[self.instructions[self.i + 1]] = self.first_input
            self.use_first_input = False
        else:
            self.instructions[self.instructions[self.i + 1]] = self.rest_input
        self.i += 2

    def _output(self, first_mode):
        if first_mode == 1:
            first_value = self.instructions[self.i + 1]
        else:
            first_value = self.instructions[self.instructions[self.i + 1]]
        self.i += 2
        return first_value

    def _jump_if_true(self, first_mode, second_mode):
        if first_mode == 1:
            first_value = self.instructions[self.i + 1]
        else:
            first_value = self.instructions[self.instructions[self.i + 1]]
        if second_mode == 1:
            second_value = self.instructions[self.i + 2]
        else:
            second_value = self.instructions[self.instructions[self.i + 2]]
        if first_value != 0:
            self.i = second_value
        else:
            self.i += 3

    def _jump_if_false(self, first_mode, second_mode):
        if first_mode == 1:
            first_value = self.instructions[self.i + 1]
        else:
            first_value = self.instructions[self.instructions[self.i + 1]]
        if second_mode == 1:
            second_value = self.instructions[self.i + 2]
        else:
            second_value = self.instructions[self.instructions[self.i + 2]]
        if first_value == 0:
            self.i = second_value
        else:
            self.i += 3

    def _less_than(self, first_mode, second_mode):
        if first_mode == 1:
            first_value = self.instructions[self.i + 1]
        else:
            first_value = self.instructions[self.instructions[self.i + 1]]
        if second_mode == 1:
            second_value = self.instructions[self.i + 2]
        else:
            second_value = self.instructions[self.instructions[self.i + 2]]
        if first_value < second_value:
            self.instructions[self.instructions[self.i + 3]] = 1
        else:
            self.instructions[self.instructions[self.i + 3]] = 0
        self.i += 4

    def _equals(self, first_mode, second_mode):
        if first_mode == 1:
            first_value = self.instructions[self.i + 1]
        else:
            first_value = self.instructions[self.instructions[self.i + 1]]
        if second_mode == 1:
            second_value = self.instructions[self.i + 2]
        else:
            second_value = self.instructions[self.instructions[self.i + 2]]
        if first_value == second_value:
            self.instructions[self.instructions[self.i + 3]] = 1
        else:
            self.instructions[self.instructions[self.i + 3]] = 0
        self.i += 4

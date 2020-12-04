class IntCode:
    OPCODE_ADD = 1
    OPCODE_MUL = 2
    OPCODE_INP = 3
    OPCODE_OUT = 4
    OPCODE_JIT = 5
    OPCODE_JIF = 6
    OPCODE_LT = 7
    OPCODE_EQ = 8
    OPCODE_RBO = 9
    OPCODE_HALT = 99

    def __init__(self, memory):
        self.memory = memory + [0] * 5000
        self.pointer = 0
        self.offset = 0
        self.first_output = True
        self.gen = self.run()
        self.gen.send(None)
        self.last_input = None

    @property
    def val(self):
        return self.memory[self.pointer]

    @property
    def opcode(self):
        return self.val % 100

    def get_mode(self, parameter):
        return self.val // 10 ** (parameter + 1) % 10

    def read(self, parameter):
        mode = self.get_mode(parameter)
        if mode == 2:
            addr = self.memory[self.pointer + parameter] + self.offset
            return self.memory[addr]
        elif mode == 1:
            value = self.memory[self.pointer + parameter]
            return value
        elif mode == 0:
            addr = self.memory[self.pointer + parameter]
            return self.memory[addr]

    def write(self, parameter, value):
        mode = self.get_mode(parameter)
        if mode == 2:
            addr = self.memory[self.pointer + parameter] + self.offset
            self.memory[addr] = value
        elif mode == 0:
            addr = self.memory[self.pointer + parameter]
            self.memory[addr] = value

    def run(self):
        while self.opcode != IntCode.OPCODE_HALT:
            if self.opcode == IntCode.OPCODE_ADD:
                self.write(3, self.read(1) + self.read(2))
                self.pointer += 4
            elif self.opcode == IntCode.OPCODE_MUL:
                self.write(3, self.read(1) * self.read(2))
                self.pointer += 4
            elif self.opcode == IntCode.OPCODE_INP:
                inp = yield
                self.last_input = inp
                self.write(1, inp)
                self.pointer += 2
            elif self.opcode == IntCode.OPCODE_OUT:
                yield self.read(1)
                self.pointer += 2
            elif self.opcode == IntCode.OPCODE_JIT:
                if self.read(1) != 0:
                    self.pointer = self.read(2)
                else:
                    self.pointer += 3
            elif self.opcode == IntCode.OPCODE_JIF:
                if self.read(1) == 0:
                    self.pointer = self.read(2)
                else:
                    self.pointer += 3
            elif self.opcode == IntCode.OPCODE_LT:
                if self.read(1) < self.read(2):
                    self.write(3, 1)
                else:
                    self.write(3, 0)
                self.pointer += 4
            elif self.opcode == IntCode.OPCODE_EQ:
                if self.read(1) == self.read(2):
                    self.write(3, 1)
                else:
                    self.write(3, 0)
                self.pointer += 4
            elif self.opcode == IntCode.OPCODE_RBO:
                self.offset += self.read(1)
                self.pointer += 2

        


